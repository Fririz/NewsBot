
import requests
from bs4 import BeautifulSoup

#URL = "https://itc.ua/techno/"
chat_id = 688419885

class prs:
    def __init__(self, URL):
        self.URL = URL

    def _get_html(self):
        response = requests.get(self.URL)
        return response.text

    def _get_articles(self):
        html = self._get_html()
        soup = BeautifulSoup(html, "html.parser")
        articles = soup.find_all("a", class_="entry-title")
        filtered = []
        for elem in articles:
            filtered.append(elem.text)
        return filtered
    
    def __str__(self):
        return self._infToString()
    
    def _infToString(self):
        articles = self._get_articles()
        infStr =""
        for elem in articles:
            infStr = infStr + elem + "\n"
        return infStr
