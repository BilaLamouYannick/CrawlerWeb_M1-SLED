from html.parser import HTMLParser
from urllib import parse
from urllib.parse import urlparse
from domain import *
import os


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # Quand nous appelons la fonction feed() de HTMLParser cette fonction s'appelle quand elle rencontre une balise <a> 
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    if (get_sub_domain_name(url) == "play.google.com"):
                        path, query = stay_domaine_search(url)
                        
                        self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass
