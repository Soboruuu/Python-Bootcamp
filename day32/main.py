import pandas as pd
import datetime as dt
import smtplib
import random

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month=now.month
day=now.day

data = pd.read_csv("birthdays.csv")
dict = data.to_dict(orient="records")

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

my_email = "YOUR_GMAIL@gmail.com"
password = "YOUR_SECRET_CODE" #<-----Gmail 앱 비밀번호로 만든 16자리 비밀번호

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)

for birthday in dict:
    if birthday['month'] == month and birthday['day'] == day:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        letter_format = random.choice(letters)
        with open(letter_format) as letter_file:
            letter = letter_file.read()
            letter_rename = letter.replace("[NAME]", birthday['name'])

# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday['email'],
                                msg=f"Subject: Happy Birthday!\n\n{letter_rename}")









