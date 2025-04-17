from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<h1>Login</h1>"

@auth.route('/logout')
def logout():
    return "<h2>Logout</h2>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"

