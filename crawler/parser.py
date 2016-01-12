from bs4 import BeautifulSoup
from crawler.item_pipeline import ItemPipeline


class Parser:
    def __init__(self, start_page):
        self.start_page = start_page

    def parse(self):
        soup = BeautifulSoup(self.start_page.text, 'lxml')
        title = soup.select("h1.publication-title")[0]

        app = ItemPipeline(title.string)
        # print(app)
        return app
