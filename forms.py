from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email
from wtforms.validators import Length


class Registration(FlaskForm):
    name = StringField('Імя', validators=[DataRequired('Не може бути пусте')])
    username = StringField('Користувач', validators=[DataRequired('Не може бути пусте')])
    password = PasswordField('Пароль', validators=[DataRequired('Не може бути пусте')])
    email = StringField('Почта', validators=[DataRequired('Не може бути пусте'), Email()])
    recomendation = StringField('Що вам подобається?',
                                validators=[DataRequired('Наприклад: Футбол, Програмування, Майнкрафт...')])
    submit = SubmitField('Підтвердити')


class LoginForm(FlaskForm):
    username = StringField('Користувач', validators=[DataRequired('Не може бути пусте')])
    password = PasswordField('Пароль', validators=[DataRequired('Не може бути пусте')])
    remember_me = BooleanField('Запамятай мене!')
    submit = SubmitField('Підтвердити')

class Search(FlaskForm):
    search_field = StringField('Пошук', validators=[Length(min=0, max=400, message='За над то багато символив'),
                                                    DataRequired('Не може бути пусте')])
    submit = SubmitField('Пошук!')
