from flask import render_template
from level_up import app, db
from flask import request,redirect,url_for,flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from level_up.models import Users, Profile, Categories, Hydration_intentions, Exercise_intentions, Sleep_intentions, Mindfulness_intentions


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("base.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        register = Users(
            username=request.form.get("username"),
            password=request.form.get("password")
        )
        db.session.add(register)
        db.session.commit()
        return redirect(url_for('register'))
        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("add_profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        user = Users.query.filter_by(username=username).first()
        if not user or not (user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for("login"))
        else:
            return redirect(url_for("dashboard"))
        
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

