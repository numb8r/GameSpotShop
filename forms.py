from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email
from wtforms.validators import Length


class Registration(FlaskForm):
    name = StringField('Username', validators=[DataRequired('Incorrect username, try again')])
    password = PasswordField('Password', validators=[DataRequired('Incorrect password, try again')])
    email = StringField('Email', validators=[DataRequired('Incorrect email, try again'), Email()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired('Incorrect username, try again')])
    password = PasswordField('Password', validators=[DataRequired('Incorrect password, try again')])
    remember_me = BooleanField('Remember me!')
    submit = SubmitField('Submit!')

# class Search(FlaskForm):
#     search_field = StringField('Пошук', validators=[Length(min=0, max=400, message='За над то багато символив'),
#                                                     DataRequired('Не може бути пусте')])
#     submit = SubmitField('Пошук!')
