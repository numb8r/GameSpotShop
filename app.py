from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user
from forms import LoginForm, Registration
from re import findall
from __init__ import User

app = Flask(__name__)
app.config["SECRET_KEY"] = '1234'
app.app_context().push()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect('index')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home_page():
    return 'Hello'

@app.route('/singup', methods=['GET', 'POST'])
def signup():
    form = Registration()
    if form.validate_on_submit():
        interests = findall('[a-z]{1,}|[а-їґ]{1,}', form.recomendation.data.lower())
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password_hash=form.password.data, interests=interests)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Ви успішно зареєструвалися!', 'succes')
        return redirect(url_for('login'))
    return render_template('authorization/register.html', title='Реєстрація', form=form)

@app.route('/log_in', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
       return redirect('index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Неправильний логін або пароль", category='error')
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect('index')
    return render_template('authorization/login.html', title='Вхід', form=form)
