from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

##FLASK_LOGIN
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        new_user = User(name=request.form['name'],
                        email=request.form['email'],
                        password=generate_password_hash(password=request.form['password'],
                                                        method='pbkdf2:sha256',
                                                        salt_length=16))
        if User.query.filter_by(email=new_user.email):
            flash("You've already signed up with that email. Log in instead!")
            return render_template('register.html')
        db.session.add(new_user)
        db.session.commit()
        return render_template('secrets.html', name=request.form['name'], logged_in=current_user.is_authenticated)
    return render_template("register.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_email = request.form.get('email')
        user = User.query.filter_by(email=user_email).first()
        if not user:
            flash('The email does not exist. Please try again.')
            return render_template('login.html')
        elif not check_password_hash(pwhash=user.password, password=request.form.get('password')):
            flash('Password incorrect. Please try again.')
            return render_template('login.html')
        else:
            login_user(user)
            return redirect(url_for('secrets', name=user.name, logged_in=current_user.is_authenticated))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
