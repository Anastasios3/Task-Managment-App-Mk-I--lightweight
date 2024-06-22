from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import Task
from forms import TaskForm
from extensions import db

task_routes = Blueprint('task', __name__)

@task_routes.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    form = TaskForm()
    sort_by = request.args.get('sort_by', 'date')
    order = request.args.get('order', 'asc')

    query = Task.query.filter_by(user_id=current_user.id)

    if sort_by == 'priority':
        query = query.order_by(Task.priority.asc() if order == 'asc' else Task.priority.desc())
    else:  # Default is sorting by date
        query = query.order_by(Task.id.asc() if order == 'asc' else Task.id.desc())

    tasks = query.all()

    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            owner=current_user
        )
        try:
            db.session.add(new_task)
            db.session.commit()
            flash('Task created!', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Error creating task: {}'.format(e), 'danger')
        return redirect(url_for('task.tasks'))

    return render_template('tasks.html', tasks=tasks, form=form)

@task_routes.route('/tasks/active')
@login_required
def active_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id, completed=False).all()
    return render_template('tasks.html', tasks=tasks, title="Active Tasks")

@task_routes.route('/tasks/completed')
@login_required
def completed_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id, completed=True).all()
    return render_template('tasks.html', tasks=tasks, title="Completed Tasks")

@task_routes.route('/tasks/all')
@login_required
def all_tasks():
    active_tasks = Task.query.filter_by(user_id=current_user.id, completed=False).all()
    completed_tasks = Task.query.filter_by(user_id=current_user.id, completed=True).all()
    return render_template('tasks.html', active_tasks=active_tasks, completed_tasks=completed_tasks, title="All Tasks")

@task_routes.route('/tasks/priority/<priority>')
@login_required
def priority_tasks(priority):
    tasks = Task.query.filter_by(user_id=current_user.id, priority=priority).all()
    return render_template('tasks.html', tasks=tasks, title=f"{priority.capitalize()} Priority Tasks")

@task_routes.route('/update_task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        return redirect(url_for('task.tasks'))
    
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.priority = form.priority.data
        db.session.commit()
        flash('Task updated!', 'success')
        return redirect(url_for('task.tasks'))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.priority.data = task.priority
    
    return render_template('update_task.html', form=form)

@task_routes.route('/delete_task/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        return redirect(url_for('task.tasks'))
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted!', 'success')
    return redirect(url_for('task.tasks'))

@task_routes.route('/complete_task/<int:task_id>', methods=['POST'])
@login_required
def complete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        flash('You do not have permission to complete this task.', 'danger')
        return redirect(url_for('task.tasks'))

    task.completed = True
    db.session.commit()
    flash('Task marked as complete!', 'success')
    return redirect(url_for('task.tasks'))
