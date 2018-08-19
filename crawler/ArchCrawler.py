from crawler.Crawler import Crawler
from bs4 import BeautifulSoup

class ArchCrawler(Crawler):
    URL = 'https://www.archdaily.com.br/br/artigos'

    def __init__(self, url = URL):
        super().__init__(url)

    def get_title(self):
        titleElement = self.elements.find('h1', {'class': 'afd-title-big'}) 
        if (titleElement == None):
            return None
        return titleElement.get_text()
    
    def get_text(self):
        article = self.elements.find('article')
        if (article == None):
            return None
        articles = article.findAll("p" , recursive=True)
        if (len(articles) == 0):
            return None
        text = ''
        for paragraphs in articles:
            text += paragraphs.get_text()
        return text

    def get_img(self):
        imgElement = self.elements.find('picture')
        if (imgElement == None):
            return None
        return imgElement.find('img')['src']