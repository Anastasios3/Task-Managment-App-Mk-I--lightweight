from flask import Flask, render_template, redirect, url_for, request, flash
from extensions import db, login_manager
from flask_login import UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress warning

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirects to the login page if the user is not logged in

# Import models and forms after initializing db and login_manager to avoid circular imports
from models import User, Task
from forms import RegistrationForm, LoginForm, TaskForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return redirect(url_for('login'))  # Redirects to the login page by default

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = form.password.data  # In real apps, use a hashing function
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:  # In real apps, check hashed passwords
            login_user(user)
            return redirect(url_for('tasks'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, description=form.description.data, owner=current_user)
        db.session.add(new_task)
        db.session.commit()
        flash('Task created!', 'success')
        return redirect(url_for('tasks'))
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=tasks, form=form)

@app.route('/update_task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        return redirect(url_for('tasks'))
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        db.session.commit()
        flash('Task updated!', 'success')
        return redirect(url_for('tasks'))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
    return render_template('update_task.html', form=form)

@app.route('/delete_task/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        return redirect(url_for('tasks'))
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted!', 'success')
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    app.run(debug=True)
