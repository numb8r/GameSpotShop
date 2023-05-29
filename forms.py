from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo
from db_control import User
from flask import flash


class Sing_up(FlaskForm):
    username = StringField('Username', validators=[DataRequired('Incorrect username, try again')])
    password = PasswordField('Password', validators=[DataRequired('Incorrect password, try again')])
    email = StringField('Email', validators=[DataRequired('Incorrect email, try again'), Email()])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Use a different username')

    def validate_username(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            flash('Use a different email')


class LoginFrom(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password1 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Remember Me!')
    submit = SubmitField('Sing in')

class AdminaddFrom(FlaskForm):
    name = StringField('Name game', validators=[DataRequired()])
    dev = StringField('Username', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Add game')