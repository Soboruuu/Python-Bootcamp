import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movie_list = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movie_list.reverse()

with open("movies.txt", "a") as file:
    for i in movie_list:
        file.write(f"{i}\n")

# movie_list[::-1]
# for n in range[len(movie_list)-1, 0, -1]:
