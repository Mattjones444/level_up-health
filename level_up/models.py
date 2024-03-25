from level_up import db
from datetime import datetime


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(128), nullable = False)

    def __repr__(self):
        return f"#{self.id} - Username:{self.username}| Password:{self.password}"

class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)


    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class My_intentions(db.Model):
    # schema for the user's intentions
    id = db.Column(db.Integer, primary_key=True)
    intention_name = db.Column(db.String(50),nullable=False)
    health_score = db.Column(db.Integer, nullable=False)
    due_date = db.Column(db.Date, nullable=False,)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


    def __repr__(self):
        return f"#{self.id} - intention_name:{self.intention_name}| health_score:{self.health_score}| due_date:{self.due_date}| user_id:{self.user.id}"



class My_completed_intentions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intention_name = db.Column(db.String(50),nullable=False)
    health_score = db.Column(db.Integer, nullable=False)
    Users_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


    def __repr__(self):
        return f"#{self.id} - intention_name:{self.intention_name}| health_score:{self.health_score}| Users_id:{self.users.id}"



class Hydration_intentions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intention_name = db.Column(db.String, unique=True, nullable=False)
    category_name = db.Column(db.String, unique=False, nullable=False)
    health_score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self



class Exercise_intentions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intention_name = db.Column(db.String, unique=True, nullable=False)
    category_name = db.Column(db.String, unique=False, nullable=False,)
    health_score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self


class Mindfulness_intentions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intention_name = db.Column(db.String, unique=True, nullable=False)
    category_name = db.Column(db.String, unique=False, nullable=False)
    health_score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self



class Sleep_intentions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intention_name = db.Column(db.String, unique=True, nullable=False)
    category_name = db.Column(db.String, unique=False, nullable=False)
    health_score = db.Column(db.Integer, nullable=False)
 
    def __repr__(self):
        return self