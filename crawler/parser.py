from bs4 import BeautifulSoup
from crawler.item_pipeline import ItemPipeline


class Parser:
    def __init__(self, start_page, uid):
        self.start_page = start_page
        self.uid = uid

    def parse(self):
        soup = BeautifulSoup(self.start_page.text, 'lxml')
        title = soup.select("h1")[0].text
        authors = soup.select("div.publication-detail-author-list  span[itemprop=name]")
        abstract = soup.select("p[itemprop=description]")[0].find_next_siblings("div")[0].text
        # links= inja biad linkhara darbiar va be item pipeline pas bedi
        app = ItemPipeline(self.uid, title, abstract, authors)
        print(app)
        return app
