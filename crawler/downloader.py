import requests
from crawler.parser import Parser


class Downloader:
    def __init__(self, link):
        self.link = link

    def get_app_from_link(self):
        start_page = requests.get(self.link)
        parser = Parser(start_page)
        parser.parse()
