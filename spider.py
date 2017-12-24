from urllib.request import urlopen
from link_finder import LinkFinder
from domain import *
from general import *
from sqlite3 import *
from roboot import Roboot
import os


class Spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name, image_file):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.image_file = image_file
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)

    # Crée le répertoire et les fichiers pour le projet sur le premier passage et commence le crawl
    @staticmethod
    def boot():
        if (os.path.exists(Spider.project_name) == False):
            create_project_dir(Spider.project_name)
            create_project_dir(Spider.image_file)
            create_data_files(Spider.project_name, Spider.base_url)
            Spider.queue = file_to_set(Spider.queue_file)
            Spider.crawled = file_to_set(Spider.crawled_file)


        # Création de la base de donnée
        if (os.path.isfile('CrawlerWeb.db') == False):
            db = connect('CrawlerWeb.db')
            db.execute('drop table if exists Application')
            db.execute('create table Application (app_name text, app_image text, app_author text, app_description text, app_developper text, app_nbInstall text, app_nbAvis text, category text)')
            db.commit()

        #if (os.path.exists(images_Application) == Fa)

    # L'affichage d'utilisateur de mises à jour, remplissages alignent et mettent des dossiers à jour
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled  ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            # modifPerso
            path = get_path_name(page_url).split('/')
            if ('details' == path[-1]):
                if ("id" in get_app_name(page_url)):
                    Spider.crawled.add(page_url)
                    Roboot(page_url)
            Spider.update_files()

    # Convertir les données crues de la variable response en information lisible et vérifie le formatage approprié de HTML 
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    # Sauvegarde les données de la file d'attente dans le fichier-projets 
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
