from flask import render_template
from level_up import app, db
from flask import request,redirect,url_for
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
    return render_template("register.html")
