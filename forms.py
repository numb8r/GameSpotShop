from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
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
    password1 = PasswordField('Repaat password', validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Remember Me!')
    submit = SubmitField('Sing in')

# class Search(FlaskForm):
#     search_field = StringField('Пошук', validators=[Length(min=0, max=400, message='За над то багато символив'),
#                                                     DataRequired('Не може бути пусте')])
#     submit = SubmitField('Пошук!')
