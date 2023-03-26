import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import string
import random
import validators

app = Flask(__name__)

############# SQL Alchemy Configuration #################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mykey'

db = SQLAlchemy(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = "login"

#######################################################

############# Create a Model #################
class Url(db.Model):
    __tablename__ ="Urls"
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_url = db.Column(db.String(10), unique=True)
    full_url = db.Column(db.String(500))

    def __init__(self, original_url, short_url,full_url):
        self.original_url = original_url
        self.short_url = short_url
        self.full_url = full_url


@app.before_first_request
def create_tables():
    db.create_all()

def shorten_url():
    chars = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(chars) for _ in range(6))
        full_url = request.host_url + short_url
        if not Url.query.filter_by(short_url=short_url).first():
            return short_url,full_url

@app.route('/add', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        if not validators.url(original_url):
            return render_template('error.html', message='Invalid URL')
        short_url, full_url = shorten_url()
        new_url = Url(original_url=original_url, short_url=short_url, full_url=full_url)
        db.session.add(new_url)
        db.session.commit()
        print(short_url)
        return render_template('result.html', short_url=full_url,original_url=original_url)
    return render_template('home.html')

@app.route('/<short_url>')
def redirect_to_original_url(short_url):
    url = Url.query.filter_by(short_url=short_url).first()
    return redirect(url.original_url)

@app.route('/history')
def history():
    urls = Url.query.all()
    return render_template('history.html', urls=urls)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

##############################################


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user = User(email=request.form.get('email'),
                    password=request.form.get('password'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Grab the user from our User Models table
        user = User.query.filter_by(email=request.form.get('email')).first()

        # Check that the user was supplied and the password is right
        # The check_password method comes from the User object
        if user is not None and user.check_password(request.form.get('password')):

            #Log in the user
            login_user(user)

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('index')

            return redirect(next)
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug = True)