from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user
# from re import findall
from db_control import User, Product
from forms import Sing_up, LoginFrom

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SECRET_KEY"] = '1234'
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

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('app.db'))
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


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        product = request.form.get('note')

        if len(product) < 1:
            flash('Product is too short!', category='error')
        else:
            new_product = Product(data=product, user_id=current_user.id)
            db.session.add(new_product)
            db.session.commit()
            flash('product added!', category='success')

    return render_template("home.html", user=current_user)




@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = Sing_up()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password_hash=form.password.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created!', category='success')
        return redirect(url_for('login'))

    return render_template("sign_up.html", user=current_user)

