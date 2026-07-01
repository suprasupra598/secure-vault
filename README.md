# SecureVault - Professional Password Manager 

SecureVault is a secure web application built with **Python (Flask)** and **SQLite**. It allows users to store and manage their digital credentials using industry-standard **AES-128 (Fernet)** encryption.

## Features
- **AES-128 Encryption:** All stored passwords are encrypted using authenticated encryption (Fernet).
- **Zero-Knowledge Principle:** The encryption key is derived from the Master Password at runtime and never stored in the database.
- **Master Password Verification:** Users must re-enter their master password to "Reveal" any saved credential.
- **Secure Hashing:** Authentication is handled via `scrypt` hashing with unique salts for every user.
- **Modern UI:** Responsive "Glassmorphism" dashboard built with Bootstrap 5.

## Technical Stack
- **Backend:** Python 3.12, Flask, Flask-SQLAlchemy
- **Security:** Cryptography (Fernet), Werkzeug Security
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, Bootstrap 5

## Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/secure-vault.git
   cd secure-vault

2. **Set up a Virtual Environment**:
`bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
3. **Install Dependencies**:
Bash
pip install -r requirements.txt
4. **Environment Variables**:
Create a .env file and add:
SECRET_KEY=your_random_secret_key
5. **Run the Application**:
Bash
python run.py
## Security Overview
This project was developed for a College Project. It emphasizes secure coding practices including CSRF protection, SQL injection prevention (via ORM), and secure key derivation using PBKDF2.

   