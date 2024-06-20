from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from models import User, Task
from forms import RegistrationForm, LoginForm, TaskForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return redirect(url_for('login'))

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
    sort_by = request.args.get('sort_by', 'date')
    order = request.args.get('order', 'asc')
    priority = request.args.get('priority', None)

    query = Task.query.filter_by(user_id=current_user.id)

    if priority:
        query = query.filter_by(priority=priority)

    if sort_by == 'priority':
        if order == 'asc':
            query = query.order_by(Task.priority.asc())
        else:
            query = query.order_by(Task.priority.desc())
    else:  # Default is sorting by date
        if order == 'asc':
            query = query.order_by(Task.id.asc())
        else:
            query = query.order_by(Task.id.desc())

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
        return redirect(url_for('tasks'))

    return render_template('tasks.html', tasks=tasks, form=form)

if __name__ == '__main__':
    app.run(debug=True)
