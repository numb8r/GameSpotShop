from flask_sqlalchemy import SQLAlchemy
# from flask_security import RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


user_roles = db.Table("user_roles",
    db.Column('user_id', db.Integer, db.ForeignKey('User.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('Role.id'))
)

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    username = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(60), index=True, unique=True)
    password_hash = db.Column(db.String)
    posts = db.relationship('Post', backref='users', lazy='dynamic', primaryjoin="User.username == Post.author")

    def has_role(self, *args):
        return set(args).issubset({role.name for role in self.roles})

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self) -> str:
        return '<User {}'.format(self.username)