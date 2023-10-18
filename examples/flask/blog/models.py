from blog import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer(), primary=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text(1000))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
