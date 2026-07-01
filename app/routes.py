from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify
from flask_login import login_required, current_user
from .models import PasswordEntry, db
from .crypto_utils import encrypt_password, decrypt_password
import secrets, string

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def dashboard():
    search = request.args.get('search', '')
    query = PasswordEntry.query.filter_by(user_id=current_user.id)
    if search:
        query = query.filter(PasswordEntry.website.contains(search))
    entries = query.all()
    return render_template('dashboard.html', entries=entries)

@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_entry():
    if request.method == 'POST':
        key = session.get('user_key').encode()
        website = request.form.get('website')
        username = request.form.get('username')
        password = request.form.get('password')
        
        encrypted = encrypt_password(password, key)
        new_entry = PasswordEntry(website=website, username_val=username, encrypted_password=encrypted, owner=current_user)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    
    # Password Generator logic
    alphabet = string.ascii_letters + string.digits + string.punctuation
    suggested = ''.join(secrets.choice(alphabet) for _ in range(16))
    return render_template('add_entry.html', suggested=suggested)

@main.route('/reveal/<int:id>', methods=['POST']) # Changed to POST
@login_required
def reveal(id):
    data = request.get_json()
    master_password = data.get('password')
    
    # 1. Verify if the Master Password is correct
    if not current_user.check_password(master_password):
        return jsonify({"error": "Incorrect Master Password"}), 401
    
    # 2. Find the entry
    entry = PasswordEntry.query.get_or_404(id)
    if entry.owner != current_user:
        return jsonify({"error": "Unauthorized"}), 403
    
    # 3. Decrypt
    try:
        key = session.get('user_key').encode()
        decrypted = decrypt_password(entry.encrypted_password, key)
        return jsonify({"password": decrypted})
    except Exception:
        return jsonify({"error": "Decryption failed"}), 500

@main.route('/delete/<int:id>')
@login_required
def delete(id):
    entry = PasswordEntry.query.get_or_404(id)
    if entry.owner == current_user:
        db.session.delete(entry)
        db.session.commit()
    return redirect(url_for('main.dashboard'))