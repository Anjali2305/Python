import requests
from bs4 import BeautifulSoup

LIST_URL = "https://www.billboard.com/charts/hot-100/"


date = input("Type date in format YYYY-MM-DD: ")

data_from_website = requests.get(f"{LIST_URL}{date}/")
webpage_html = data_from_website.text 


soup = BeautifulSoup(webpage_html, "html.parser")
print(soup.title)
titles = soup.select(selector="li ul li  h3", class_="c-title")
artists = soup.select(selector="li ul li  span", class_="c-label ")
song_titles = []
song_artists = []
for artist in artists:
    song_artists.append(artist.get_text())
for title in titles:
    song_titles.append(title.get_text())
print(song_titles)
print(song_artists)



