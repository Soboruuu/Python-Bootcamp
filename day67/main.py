from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField('Body')
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts=db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)

@app.route('/new-post', methods=['GET','POST'])
def make_new_post():
    post_form = CreatePostForm()
    if post_form.validate_on_submit():
        new_post=BlogPost(title=post_form.title.data,
                          subtitle=post_form.subtitle.data,
                          date=date.today().strftime('%B %d %Y'),
                          author=post_form.author.data,
                          img_url=post_form.img_url.data,
                          body=post_form.body.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=post_form)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)

@app.route('/edit/<int:post_id>', methods=['GET','POST'])
def edit_post(post_id):
    post_to_edit = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(title=post_to_edit.title,
                               subtitle=post_to_edit.subtitle,
                               author=post_to_edit.author,
                               img_url=post_to_edit.img_url,
                               body=post_to_edit.body)
    if edit_form.validate_on_submit():
        post_to_edit.title=edit_form.title.data
        post_to_edit.subtitle=edit_form.subtitle.data
        post_to_edit.author=edit_form.author.data
        post_to_edit.img_url=edit_form.img_url.data
        post_to_edit.body=edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_to_edit.id))
    return render_template("make-post.html", form=edit_form, is_new=False)

@app.route("/delete/<int:post_id>")
def delete(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=5002)