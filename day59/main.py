from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/9475b5ad8d2396fdafc7")
data = response.json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def blog_post(num):
    requested_post = 0
    for post in data:
        if post["id"] == num:
            requested_post = post
    return render_template("post.html", blog_post=requested_post)


if __name__ == "__main__":
    app.run(debug= True, port=5001)