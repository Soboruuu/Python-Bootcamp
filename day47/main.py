import requests
from bs4 import BeautifulSoup
import smtplib


PRODUCT="YOUR_AMAZON_TARGET_ITEM"
my_email="YOUR_GMAIL@gmail.com"
password="YOUR_GMAIL_PASSWORD"


response = requests.get(PRODUCT,
                        headers={"Accept-Language":"ko,en-US;q=0.9,en;q=0.8,sv;q=0.7,ja;q=0.6",
                                 "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
soup = BeautifulSoup(response.text, "html.parser")

TARGET_PRICE=YOUR_TARGET_PRICE
price = float(soup.find(name="span", class_="a-offscreen").getText().strip("$"))
print(price)

if price < TARGET_PRICE:
    product_name = soup.select_one(selector="#title > #productTitle").getText()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Low Price alert!\n\n"
                                f"{product_name}\n"
                                f"is now ${price}!!!"
                                f"\nCheck out the link."
                                f"\n{PRODUCT}")
