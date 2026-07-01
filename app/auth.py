from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required
from .models import User, db
from .crypto_utils import derive_key

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('auth.register'))
        
        new_user = User(username=username)
        new_user.set_password(password) # This sets the hash and the salt
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please login.')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        # This is where the AttributeError usually happens
        if user and user.check_password(password):
            login_user(user)
            # Derive the key and store in session for encryption/decryption
            user_key = derive_key(password, user.salt)
            session['user_key'] = user_key.decode()
            return redirect(url_for('main.dashboard'))
        
        flash('Invalid username or password')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    session.pop('user_key', None)
    logout_user()
    return redirect(url_for('auth.login'))