from tkinter import *
import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

class CrawlerWeb:

    def __init__(self, fenetre, projet_name, homepage, domain_name, queue_file, crawled_file, image_file, width = 200, height = 200, bg = "white"):

        self.fenetre = fenetre
        self.PROJECT_NAME = projet_name
        self.HOMEPAGE = homepage
        self.DOMAIN_NAME = domain_name
        self.QUEUE_FILE = queue_file
        self.CRAWLED_FILE = crawled_file
        self.IMAGE_FILE = image_file
        self.NUMBER_OF_THREADS = 10
        self.queue = Queue()
        Spider(self.PROJECT_NAME, self.HOMEPAGE, self.DOMAIN_NAME, self.IMAGE_FILE)

        self.fenetre.title("CrawlerWeb By SBLY")
        button = Menubutton(self.fenetre, text = 'Main')
        button.pack(side = LEFT)
        menuFile = Menu(button)
        menuFile.add_command(label = 'Crawler', command = self.main())


    # Creation des threads
    def create_workers(self):
        for _ in range(self.NUMBER_OF_THREADS):
            t = threading.Thread(target=self.work)
            t.daemon = True
            t.start()


    # Faites le prochain travail dans la file d'attente 
    def work(self):
        while True:
            url = self.queue.get()
            Spider.crawl_page(threading.current_thread().name, url)
            self.queue.task_done()


    # Chaque lien aligné est un nouveau travail
    def create_jobs(self):
        for link in file_to_set(self.QUEUE_FILE):
            self.queue.put(link)
        self.queue.join()
        self.crawl()


    # Contrôlez s'il y a des éléments dans la file d'attente, crawl s'il y en a 
    def crawl(self):
        queued_links = file_to_set(self.QUEUE_FILE)
        if len(queued_links) > 0:
            print(str(len(queued_links)) + ' links in the queue')
            self.create_jobs()

    def main(self):
        self.create_workers()
        self.crawl()

if __name__ == '__main__':
    projet_name = 'google_crawl'
    homepage = 'https://play.google.com/store/search?q=cameroun&c=apps'
    domain_name = get_domain_name(homepage)
    queue_file = projet_name + '/queue.txt'
    crawled_file = projet_name + '/crawled.txt'
    image_file = 'images_Application'
    fenetre = Tk()
    CrawlerWeb = CrawlerWeb(fenetre, projet_name, homepage, domain_name, queue_file, crawled_file, image_file)
    fenetre.mainloop()