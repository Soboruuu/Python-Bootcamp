# import requests
# from bs4 import BeautifulSoup
# import csv
#
# URL=f"https://store.nintendo.co.kr/games/sale"
#
# response = requests.get(URL,
#                         headers={"Accept-Language":"ko,en-US;q=0.9,en;q=0.8,sv;q=0.7,ja;q=0.6",
#                                  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})
#
# soup = BeautifulSoup(response.text, "html.parser")
# titles = soup.find_all(class_='category-product-item-title-link')
# prices = soup.find_all(class_='special-price')
# old_prices = soup.find_all(class_='old-price')
#
#
# for i in range(100):
#     number = f'{i+1}.'
#     title = titles[i].get_text().strip()
#     old_price = old_prices[i].get_text().strip()
#     price = prices[i].get_text().strip('\n\nSpecial Price\n')
#     print(f'{number} {title}')
#     print(f'{old_price}\n->\n{price}\n')


import requests
from bs4 import BeautifulSoup
import csv

URL = "https://store.nintendo.co.kr/games/sale"

response = requests.get(URL, headers={
    "Accept-Language": "ko,en-US;q=0.9,en;q=0.8,sv;q=0.7,ja;q=0.6",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
})

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all(class_='category-product-item-title-link')
prices = soup.find_all(class_='special-price')
old_prices = soup.find_all(class_='old-price')

rows = []
for i in range(100):
    number = f'{i+1}.'
    title = titles[i].get_text().strip()
    old_price = old_prices[i].get_text().strip('정가\n')
    price = prices[i].get_text().strip('\n\nSpecial Price\n')
    rows.append([number, title, old_price, price])

# Save the data to a CSV file
with open('nintendo_sale.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['No.', 'Title', 'Original Price', 'Special Price'])
    writer.writerows(rows)