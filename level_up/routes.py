from flask import render_template
from level_up import app, db
from level_up.models import Users, Profile, Categories, Hydration_intentions, Exercise_intentions, Sleep_intentions, Mindfulness_intentions


@app.route("/")
@app.route("/home_page")
def home_page():
    return render_template("base.html")