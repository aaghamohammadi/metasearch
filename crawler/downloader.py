import requests
from crawler.parser import Parser
import re
import json
from pprint import pprint


class Downloader:
    def __init__(self, link):
        self.link = link

    def get_app_from_link(self):
        uid = int(re.search(r'\d+', self.link).group())
        start_page = requests.get(self.link)
        parser = Parser(start_page, uid)
        app = parser.parse()
        # headers = {
        #     'accept': 'application/json',
        #     'x-requested-with': 'XMLHttpRequest'
        # }
        #
        # js_resource_url = 'https://www.researchgate.net/publicliterature.PublicationCitationsList.html?' \
        #                   'publicationUid=' + str(uid) + '&showCitationsSorter=true' \
        #                                                  '&showAbstract=true&showType=true&showPublicationPreview=true' \
        #                                                  '&swapJournalAndAuthorPositions=false'
        # # r = requests.get(js_resource_url, headers=headers)
        # pprint(json.loads(r.text))

        return app
