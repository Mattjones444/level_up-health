from flask import render_template
from level_up import app, db
from flask import request,redirect,url_for,flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey
from level_up.models import Users, Profile, Category, Hydration_intentions, Exercise_intentions, Sleep_intentions, Mindfulness_intentions


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
            session["username"] = username
            return redirect(url_for("dashboard"))
        
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]

    return render_template("dashboard.html", username=username)

    return render_template("dashboard.html")

@app.route("/choose_intention")
def choose_intention():
    return render_template("choose_intention.html")

@app.route("/exercise_intention")
def exercise_intention():
    return render_template("exercise_intention.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("choose_intention"))
    return render_template("add_intention.html", categories=categories)

@app.route("/add_intention", methods=["GET", "POST"])
def add_intention():
    if request.method == "POST":
        new_intention = Hydration_intentions(    
            intention_name=request.form.get("intention_name"),
            category_name=request.form.get("category_name"),
            health_score=request.form.get("health_score")
        )
        db.session.add(new_intention)
        db.session.commit()
        return redirect(url_for("add_intention"))
    return render_template("add_intention.html", new_intention=new_intention)


@app.route("/hydration_intentions")
def hydration_intentions():
    return render_template("hydration_intentions.html")



    
