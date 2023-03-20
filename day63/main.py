from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy, session, query

db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.FLOAT, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Books).all()
    return render_template('index.html', books = all_books)

@app.route("/add", methods=['GET','POST'])
def add():
    if request.method== 'POST':
        new_book = Books(title=request.form['title'],
                    author= request.form['author'],
                    rating= request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    id = request.args.get('id')
    book_selected = Books.query.get(id)
    return render_template('edit_rating.html', book=book_selected)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    book_to_delete = Books.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
