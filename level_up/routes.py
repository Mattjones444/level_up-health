from flask import render_template
from level_up import app, db
from flask import request,redirect,url_for,flash,session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey
from datetime import datetime
from level_up.models import Users, Category, Hydration_intentions, Exercise_intentions, Sleep_intentions, Mindfulness_intentions, My_intentions, My_completed_intentions


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
                session["user"] = request.form.get("username")
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
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]
    
    total_intentions_count = My_completed_intentions.query.count()

    total_health_scores = db.session.query(db.func.sum(My_completed_intentions.health_score)).scalar()

    average_health_score = db.session.query(db.func.avg(My_completed_intentions.health_score)).scalar()

    return render_template("dashboard.html", username=session["user"],total_intentions_count=total_intentions_count,total_health_scores=total_health_scores, average_health_score=average_health_score)


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
def my_intentions():
    exercise = list(Exercise_intentions.query.order_by(Exercise_intentions.intention_name).all())
    new = None 

    if request.method == "POST":
        user = Users.query.filter_by().first()
        users_id = user.id

        new = My_intentions(
        intention_name=request.form.get("intention_name"),
        health_score=request.form.get("health_score"),
        due_date=datetime.strptime(request.form['due_date'], '%b %d, %Y').date(),
        Users_id=users_id
        )
        
        db.session.add(new)
        db.session.commit()
    
    return render_template("my_intentions.html", exercise=exercise, new=new)


@app.route("/show_intentions")
def show_intentions():
    user_intentions = list(My_intentions.query.order_by(My_intentions.intention_name).all())
    return render_template("my_intentions.html", user_intentions=user_intentions)


@app.route("/my_completed_intentions", methods=["GET", "POST"])
def my_completed_intentions():
    completed_intention = None 
    exercise = list(Exercise_intentions.query.order_by(Exercise_intentions.intention_name).all())

    if request.method == "POST":
        user = Users.query.filter_by().first()
        users_id = user.id

        completed_intention = My_completed_intentions(
        intention_name=request.form.get("intention_name"),
        health_score=request.form.get("health_score"),
        Users_id=users_id
        )
        
        db.session.add(completed_intention)
        db.session.commit()

    completed_intention = My_completed_intentions.query.all()

    return render_template("completed_intentions.html", completed_intention=completed_intention)


@app.route("/delete_intention/<int:intention_id>", methods=["GET", "POST"])
def delete_intention(intention_id):
    intention_to_delete = My_intentions.query.get(intention_id)
    if intention_to_delete:
        db.session.delete(intention_to_delete)
        db.session.commit()
        return redirect(url_for("my_intentions"))
    







