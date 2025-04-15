

import telebot
from secr import TOKEN 
import requests
from bs4 import BeautifulSoup

#bot = telebot.TeleBot(TOKEN)



URL = "https://itc.ua/techno/"


def get_html(url):
    response = requests.get(url)
    return response.text

def get_articles(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("a", class_="entry-title")
    filtered = []
    for elem in articles:
        filtered.append(elem.text)
    return filtered

def main():
    html = get_html(URL)
    articles = get_articles(html)
    for elem in articles:
        print(elem + "\n")

if __name__ == "__main__":
    main()