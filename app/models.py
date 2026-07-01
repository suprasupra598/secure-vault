from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import os

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    salt = db.Column(db.LargeBinary, nullable=False)
    entries = db.relationship('PasswordEntry', backref='owner', lazy=True)

    def set_password(self, password):
        # We store the hash of the password
        self.password_hash = generate_password_hash(password)
        # We generate a unique salt for this user's encryption key
        self.salt = os.urandom(16)

    def check_password(self, password):
        # This compares the typed password with the stored hash
        return check_password_hash(self.password_hash, password)

class PasswordEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(120), nullable=False)
    username_val = db.Column(db.String(120), nullable=False)
    encrypted_password = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)