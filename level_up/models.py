from level_up import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(20), unique =True, nullable = False)

    def __repr__(self):
        return f"#{self.id} - Username:{self.username}| Password:{self.password}"


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    weight = db.Column(db.Integer, unique=False, nullable=False)
    smoker = db.Column(db.Boolean, default=False, nullable=False)
    my_intentions = db.Column(db.String, unique=True, nullable=False)

    
    def __repr__(self):
        return f"#{self.id} - Name:{self.name}| Age:{self.age}| Height:{self.height}| Weight:{self.weight}| Smoker:{self.smoker}| My Intentions:{my_intentions}"



class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hydration = db.Column(db.String, unique=True, nullable=False)
    exercise = db.Column(db.String, unique=True, nullable=False)
    mindfulness = db.Column(db.String, unique=True, nullable=False)
    sleep = db.Column(db.String, unique=True, nullable=False)


    def __repr__(self):
        return f"#{self.id} - Hydration:{self.hydration}| Exercise:{self.exercise}| Mindfulness:{self.mindfulness}| Sleep:{self.sleep}"



class Hydration_intentions(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return self



class Exercise_intentions(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return self


class Mindfulness_intentions(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return self



class Sleep_intentions(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return self