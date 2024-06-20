from flask import Blueprint, redirect, url_for

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return redirect(url_for('auth.login'))
