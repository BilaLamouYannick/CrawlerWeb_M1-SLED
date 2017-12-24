import os
from sqlite3 import *
from urllib.request import urlopen
import bs4 as BeautifulSoup
from application import Application
from general import *



# Il permet de chercher les applications et sauvegarder
class Roboot:

    App = set()
    
    def __init__(self, page_url):
        self.Search_application(page_url)

    # La fonction qui cherche les informations sur l'application
    def Search_application(self, page_url):
        App = Application(page_url)
        Roboot.Save_application(App)

    # La fonction qui sauvegarde les données dans la base de donnée
    def Save_application(App):
        db = connect('CrawlerWeb.db')
        cursor = db.cursor()
        cursor.execute(""" INSERT INTO Application(app_name, app_image, app_author, app_description, app_developper, app_nbInstall, app_nbAvis, category) VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", (App.name, App.img_name, App.author, App.description, App.developper, App.nbInstall, App.nbAvis, App.category))
        db.commit()
