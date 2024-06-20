from flask import Flask
from extensions import db, login_manager
from config import Config
from models import User, Task
from routes import main_routes, auth_routes, task_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(main_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(task_routes)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
