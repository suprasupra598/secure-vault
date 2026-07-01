#  SecureVault - Advanced AES-Encrypted Password Manager

SecureVault is a production-grade password management web application built with **Python (Flask)** and **SQLite**. This project demonstrates a "Zero-Knowledge" security architecture where sensitive data is encrypted using **AES-128 (Fernet)** before being stored in the database.

---

##  Key Features
- **Zero-Knowledge Security:** Encryption keys are derived from the Master Password at runtime and are never stored in the database.
- **AES-128 Encryption:** Utilizes the Python Cryptography library for robust, authenticated encryption.
- **Step-Up Authentication:** Requires a Master Password confirmation before revealing sensitive credentials.
- **Secure Hashing:** Protects login credentials using `scrypt` hashing with unique user salts.
- **Modern UI:** Responsive "Glassmorphism" dashboard designed with Bootstrap 5.

---

##  Technical Stack
- **Backend:** Python 3.12, Flask, Flask-SQLAlchemy
- **Security:** Cryptography (Fernet), Werkzeug Security
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, Bootstrap 5

---

##  Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/suprasupra598/secure-vault.git
cd secure-vault
2. Set up a Virtual Environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables
Create a file named .env in the root directory and add your secret key:
SECRET_KEY=your_random_secret_key_here
5. Run the Application
python run.py

**Security Overview**
Developed as a Final Year College Project, SecureVault emphasizes industry-standard security practices:
CSRF Protection: Implemented via Flask-WTF to prevent cross-site request forgery.
SQL Injection Prevention: All database operations use SQLAlchemy ORM to sanitize inputs.
Key Derivation: Uses PBKDF2 with 100,000 iterations to derive encryption keys from user passwords.
