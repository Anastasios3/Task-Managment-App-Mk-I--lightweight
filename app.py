from flask import Flask
from extensions import db, login_manager
from models.user import User
from routes.auth_routes import auth_bp
from routes.main_routes import main_bp
from routes.task_routes import task_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_manager.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(task_routes)

if __name__ == '__main__':
    app.run(debug=True)
