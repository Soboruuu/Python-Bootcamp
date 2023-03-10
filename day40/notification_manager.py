import smtplib

EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "YOUR@EMAIL.ADDRESS"
MY_PASSWORD = "YOUR EMAIL APP PASSWORD 16자리" #<-----Gmail 앱 비밀번호로 만든 16자리 비밀번호

    def send_emails(self, emails, message):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8'))
