import os
from sqlite3 import *
from urllib.request import urlopen, urlretrieve
import bs4 as BeautifulSoup
from general import *
import re

class Application:

    name = ''
    image = ''
    author = ''
    description = ''
    developper = ''
    nbInstall = ''
    nbAvis = ''
    category = ''
    App =  set()

    def __init__(self, page_url):
        self.Search_application(page_url)

    # La fonction qui cherche les informations sur l'application
    def Search_application(self, page_url):
        try:
            app_url = urlopen(page_url)
            html_string = BeautifulSoup.BeautifulSoup(app_url, 'html.parser')
            self.name = html_string.find("div", {"class": "id-app-title"}).get_text()
            image = html_string.find("img", {"class": "cover-image"})['src']
            name = re.sub('\W', '', self.name) # pour retire les ' : etc '
            self.img_name, header = urlretrieve('http:'+image, filename = 'images_Application/' + name + '.png')
            self.author = html_string.find("div", {"class": "content", "itemprop":""}).get_text()
            self.description = html_string.find("div", {"jsname": "C4s9Ed"}).get_text()
            self.developper = html_string.find("a", {"class": "dev-link"})['href'].split(':')[-1]
            self.nbInstall = html_string.find("div", {"class": "content", "itemprop": "numDownloads"}).get_text()
            self.nbAvis = html_string.find("div", {"class": "score"}).get_text()
            self.category = html_string.find("span", {"itemprop": "genre"}).get_text()
        except:
            return ''
