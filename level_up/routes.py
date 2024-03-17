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
        # check if username already exists in db
        existing_user = Users.query.filter_by(username=request.form.get("username").lower()).first()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        new_user = Users(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(new_user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("dashboard", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = Users.query.filter_by(username=request.form.get("username").lower()).first()

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user.password, request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("dashboard", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("username")
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]

    return render_template("dashboard.html", username=session["user"])

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
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        new_intention = Exercise_intentions(    
            intention_name=request.form.get("intention_name"),
            category_name=request.form.get("category_name"),
            health_score=request.form.get("health_score")
        )
        db.session.add(new_intention)
        db.session.commit()
        return redirect(url_for("add_intention"))
    return render_template("add_intention.html", categories=categories)


@app.route("/hydration_intentions")
def hydration_intentions():
    hydration = list(Hydration_intentions.query.order_by(Hydration_intentions.intention_name).all())
    return render_template("hydration_intentions.html", hydration=hydration)


@app.route("/mindfulness_intentions")
def mindfulness_intentions():
    mindfulness = list(Mindfulness_intentions.query.order_by(Mindfulness_intentions.intention_name).all())
    return render_template("mindfulness_intentions.html", mindfulness=mindfulness)

@app.route("/sleep_intentions")
def sleep_intentions():
    sleep = list(Sleep_intentions.query.order_by(Sleep_intentions.intention_name).all())
    return render_template("sleep_intentions.html", sleep=sleep)

@app.route("/exercise_intentions")
def exercise_intentions():
    exercise = list(Exercise_intentions.query.order_by(Exercise_intentions.intention_name).all())
    return render_template("exercise_intentions.html", exercise=exercise)


@app.route("/my_intentions", methods=["GET", "POST"])
def my_intentions(exercise_intention_id):
    exercise = list(Exercise_intentions.query.order_by(Exercise_intentions.intention_name).all())
    if request.method == "POST":
        new=My_intentions(
            intention_name=request.form.get("intention_name"),
            health_score=request.form.get("health_score"),
            due_date=request.form.get("due_date")
        )
        db.session.add(new)
        db.session.commit()
    
    return render_template("my_intentions.html", exercise=exercise)