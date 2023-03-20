from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = "YOUREMAIL@gmail.com"
PASSWORD = "abcdefghijklmnop" #<-----Gmail 앱 비밀번호로 만든 16자리 비밀번호


response = requests.get("https://api.npoint.io/9475b5ad8d2396fdafc7")
data = response.json()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", posts=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form['username'])
        print(request.form['email'])
        print(request.form['phonenumber'])
        print(request.form['message'])
        send_message(request.form['username'],request.form['email'],request.form['phonenumber'],request.form['message'])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_message(name,email,phone,message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=email_message)

@app.route("/post/<int:num>")
def blog_post(num):
    requested_post = 0
    for post in data:
        if post["id"] == num:
            requested_post = post
    return render_template("post.html", blog_post=requested_post)


if __name__ == "__main__":
    app.run(debug= True, port=5001)
