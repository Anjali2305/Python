from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.findAll(name="a", class_="titlelink")

article_text = []
article_link = []
for article in articles:
    text = article.get_text()
    link = article.get("href")
    article_text.append(text)
    article_link.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.findAll(name="span", class_ ="score")]


print(article_text)
print(article_upvotes)
print(article_link)

largest_number = max(article_upvotes)
largest_number_index = article_upvotes.index(largest_number)
print(largest_number)
print(article_text[largest_number_index])
print(article_link[largest_number_index])