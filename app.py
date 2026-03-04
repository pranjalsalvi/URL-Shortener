from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import string
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ==============================
# DATABASE MODELS
# ==============================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    urls = db.relationship('URL', backref='owner', lazy=True)


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(6), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# ==============================
# HELPER FUNCTION
# ==============================

def generate_short_code():
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(6))
        if not URL.query.filter_by(short_code=short_code).first():
            return short_code


# ==============================
# ROUTES
# ==============================

@app.route('/')
def home():
    return render_template("home.html")


# ------------------------------
# SIGNUP
# ------------------------------
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')

    if not name or not username or not password:
        flash("All fields are required")
        return redirect(url_for('home'))

    if len(password) < 6:
        flash("Password must be at least 6 characters long")
        return redirect(url_for('home'))

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        flash("Username already exists")
        return redirect(url_for('home'))

    hashed_password = generate_password_hash(password)

    new_user = User(
        name=name,
        username=username,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    flash("Account created successfully! Please login.")
    return redirect(url_for('home'))
# ------------------------------
# LOGIN
# ------------------------------
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        flash("Please enter username and password")
        return redirect(url_for('home'))

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        session['username'] = user.username
        session['name'] = user.name
        flash("Login successful!")
        return redirect(url_for('dashboard'))

    flash("Invalid Username or Password")
    return redirect(url_for('home'))


# ------------------------------
# DASHBOARD
# ------------------------------
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        flash("Please login first")
        return redirect(url_for('home'))

    if request.method == "POST":
        original_url = request.form.get('original_url')

        if not original_url:
            flash("Please enter a valid URL")
            return redirect(url_for('dashboard'))

        short_code = generate_short_code()

        new_url = URL(
            original_url=original_url,
            short_code=short_code,
            user_id=session['user_id']
        )

        db.session.add(new_url)
        db.session.commit()

        flash("Short URL created successfully!")

    user_urls = URL.query.filter_by(user_id=session['user_id']).all()
    return render_template("dashboard.html", urls=user_urls)


@app.route('/delete/<int:url_id>', methods=['POST'])
def delete_link(url_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # 1. Find the link in the database
    # (Example using SQLAlchemy: adjust if using raw SQL or another ORM)
    url_to_delete = URL.query.get_or_404(url_id)

    # 2. Security Check: Ensure the link belongs to the logged-in user
    if url_to_delete.user_id != session['user_id']:
        return "Unauthorized", 403

    # 3. Delete and Save
    db.session.delete(url_to_delete)
    db.session.commit()

    return redirect(url_for('dashboard'))
# ------------------------------
# REDIRECT SHORT URL
# ------------------------------
@app.route('/<short_code>')
def redirect_to_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first()

    if url:
        return redirect(url.original_url)

    return "Invalid URL", 404


# ------------------------------
# LOGOUT
# ------------------------------
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully")
    return redirect(url_for('home'))


# ==============================
# RUN APP
# ==============================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)