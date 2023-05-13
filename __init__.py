from flask_sqlalchemy import SQLAlchemy
# from flask_security import RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String)
    posts = db.relationship('Post', backref='users', lazy='dynamic', primaryjoin="User.username == Post.author")


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self) -> str:
        return '<User {}'.format(self.username)

class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    price = db.Column(db.Integer, index=True)