from flask import Flask, render_template, redirect, url_for, flash, request ,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, login_required
from db_control import User, Games
from forms import Sing_up, LoginFrom, AdminaddFrom

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SECRET_KEY"] = '1234'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'


@app.route('/')
@app.route('/index/')
def index():
    authenticated = True
    if current_user.is_authenticated:
        authenticated = False
    return render_template('index.html', title='Home', authenticated=authenticated)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))

    return render_template("login.html", title="Login", form=form)


@app.route('/sing_up', methods=['GET', 'POST'])
def sign_up():
    form = Sing_up()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created!', category='success')
        return redirect(url_for('login'))
    return render_template('sing_up.html', title='Sing up', form=form)

@app.route('/Game/<game>')
@login_required
def game(game):
    game = Games.query.filter_by(name=game).first()

@app.route('/add_items', methods=['GET', 'POST'])
def add_items():
    form = AdminaddFrom()
    if current_user.username == 'Admin':
        if form.validate_on_submit():
            add_prod = Games(name=form.name.data, price=form.price.data, developer=form.dev.data,
                                genre=form.genre.data)
            db.session.add(add_prod)
            db.session.commit()
            return redirect(url_for('index'))
    else:
        flash('You is admin : )')
    return render_template('add_items.html', form=form, title='Add Games')