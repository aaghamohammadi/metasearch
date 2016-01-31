from bs4 import BeautifulSoup
from crawler.item_pipeline import ItemPipeline
import requests
import json
from pprint import pprint

class Parser:
    def __init__(self, start_page, uid):
        self.start_page = start_page
        self.uid = uid


    def extract_in_links(self):
        links = []

        headers = {
             'accept': 'application/json',
             'x-requested-with': 'XMLHttpRequest'
        }

        #for cited-in s
        js_resource_url = 'http://www.researchgate.net/publicliterature.PublicationIncomingCitationsList.html?' \
                           'publicationUid=' + str(self.uid) + '&showCitationsSorter=true' \
                                                          '&showAbstract=true&showType=true&showPublicationPreview=true' \
                                                          '&swapJournalAndAuthorPositions=false'
        r = requests.get(js_resource_url, headers=headers)
        for jreq in json.loads(r.text)['result']['data']['citationItems']:
            links.append(str('http://www.researchgate.net/' + jreq['data']['publicationUrl']))


        return links


    def extract_out_links(self):
        links = []

        headers = {
             'accept': 'application/json',
             'x-requested-with': 'XMLHttpRequest'
        }

        #for references
        js_resource_url = 'http://www.researchgate.net/publicliterature.PublicationCitationsList.html?' \
                           'publicationUid=' + str(self.uid) + '&showCitationsSorter=true' \
                                                          '&showAbstract=true&showType=true&showPublicationPreview=true' \
                                                          '&swapJournalAndAuthorPositions=false'
        r = requests.get(js_resource_url, headers=headers)
        for jreq in json.loads(r.text)['result']['data']['citationItems']:
            links.append(str('http://www.researchgate.net/' + jreq['data']['publicationUrl']))


        return links


    def parse(self):
        try:
            soup = BeautifulSoup(self.start_page.text, 'lxml')
            title = soup.select("h1")[0].text
            authors = soup.select("div.publication-detail-author-list  span[itemprop=name]")
            abstract = soup.select("p[itemprop=description]")[0].find_next_siblings("div")[0].text

            out_links = self.extract_out_links()
            in_links = self.extract_in_links()


            app = ItemPipeline(self.uid, title, abstract, authors, in_links, out_links)

        except:
            return 0

        print(app)
        return app
