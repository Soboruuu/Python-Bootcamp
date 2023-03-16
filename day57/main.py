from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
data = response.json()

@app.route('/')
def home():
    return render_template("index.html", blog_data=data)

@app.route('/post/<int:num>')
def blog_post(num):
    return render_template("post.html", blog_data=data, post_num=num)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
