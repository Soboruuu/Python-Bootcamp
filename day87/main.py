from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, URL


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#DB Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

# WTForms Configuration
choices = ['✅', '❌']

class Form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    map_url = URLField('Map Link', validators=[DataRequired(), URL()])
    img_url = URLField('Image Link', validators=[DataRequired(), URL()])
    location = StringField('Location', validators=[DataRequired()])
    has_sockets = SelectField('Has Sockets', choices=choices, validators=[DataRequired()])
    has_toilet = SelectField('Has Toilet', choices=choices, validators=[DataRequired()])
    has_wifi = SelectField('Has Wifi', choices=choices,validators=[DataRequired()])
    can_take_calls = SelectField('Can Take Calls', choices=choices, validators=[DataRequired()])
    seats = StringField('Seats', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price', validators=[DataRequired()])
    submit = SubmitField("Add")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cafes')
def cafes():
    all_cafes = db.session.query(Cafe).all()
    return render_template('cafes.html', cafes=all_cafes)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = Form()
    if form.validate_on_submit():
        new_cafe = Cafe(name=form.name.data,
                        map_url=form.map_url.data,
                        img_url=form.img_url.data,
                        location=form.location.data,
                        has_sockets=bool(1 if form.has_sockets.data == '✅' else 0),
                        has_toilet=bool(1 if form.has_toilet.data == '✅' else 0),
                        has_wifi=bool(1 if form.has_wifi.data == '✅' else 0),
                        can_take_calls=bool(1 if form.can_take_calls.data == '✅' else 0),
                        seats=form.seats.data,
                        coffee_price=form.coffee_price.data,)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/update', methods=['POST', 'GET', 'PATCH'])
def update():
    cafe_id = request.args.get('id')
    selected_cafe = Cafe.query.get(cafe_id)
    form = Form(
        name=selected_cafe.name,
        map_url=selected_cafe.map_url,
        img_url=selected_cafe.img_url,
        location=selected_cafe.location,
        seats=selected_cafe.seats,
        coffee_price=selected_cafe.coffee_price)
    if form.validate_on_submit():
        has_sockets = bool(1 if form.has_sockets.data == '✅' else 0)
        has_toilet = bool(1 if form.has_toilet.data == '✅' else 0)
        has_wifi = bool(1 if form.has_wifi.data == '✅' else 0)
        can_take_calls = bool(1 if form.can_take_calls.data == '✅' else 0)

        selected_cafe.name = form.name.data
        selected_cafe.map_url=form.map_url.data
        selected_cafe.img_url=form.img_url.data
        selected_cafe.location=form.location.data
        selected_cafe.has_sockets = has_sockets
        selected_cafe.has_toilet = has_toilet
        selected_cafe.has_wifi = has_wifi
        selected_cafe.can_take_calls = can_take_calls
        selected_cafe.seats = form.seats.data
        selected_cafe.coffee_price = form.coffee_price.data

        db.session.commit()
        return redirect(url_for('cafes'))
    return render_template('update.html', form=form)


@app.route('/delete')
def delete():
    cafe_id = request.args.get('id')
    selected_cafe = Cafe.query.get(cafe_id)
    db.session.delete(selected_cafe)
    db.session.commit()
    return redirect(url_for('cafes'))

if __name__ == "__main__":
    app.run(debug=True, port=5001)