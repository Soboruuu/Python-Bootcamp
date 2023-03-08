import smtplib
import datetime as dt
import random

my_email = "YOUREMAIL@gmail.com"
password = "YOUR_SECRET_CODE" #<-----Gmail 앱 비밀번호로 만든 16자리 비밀번호

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quotes_data:
        quotes = quotes_data.readlines()
        todaysquote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="EMAIL@EMAIL.com",
                            msg=f"Subject: Monday Motivation"
                                f"\n\n{todaysquote}"
                            )


