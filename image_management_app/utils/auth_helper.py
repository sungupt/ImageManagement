
import bcrypt

users = {}  # Simple in-memory store, use a database in production

# Register a new user
def register_user(username, password):
    if username in users:
        return False
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = hashed_pw
    return True

# Login user
def login_user(username, password):
    if username in users:
        hashed_pw = users[username]
        return bcrypt.checkpw(password.encode('utf-8'), hashed_pw)
    return False

# Authentication decorator
from functools import wraps
from flask import redirect, url_for, session

def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
