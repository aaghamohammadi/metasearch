import requests
from crawler.parser import Parser
import re




class Downloader:
    def __init__(self, link):
        self.link = link

    def get_app_from_link(self):
        uid = int(re.search(r'\d+', self.link).group())
        start_page = requests.get(self.link)
        parser = Parser(start_page, uid)
        app = parser.parse()


        return app
