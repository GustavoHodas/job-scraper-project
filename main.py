import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quote_blocks = soup.find_all("div", class_="quote")

with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["Quote", "Author"])

    for block in quote_blocks:
        quote = block.find("span", class_="text").text
        author = block.find("small", class_="author").text

        print(f"{quote} - {author}")
        writer.writerow([quote, author])