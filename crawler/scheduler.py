from crawler.downloader import Downloader
from elasticSearch import searcher
import json

class Scheduler:
    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.current_depth = 0
        self.depth_links = []
        self.apps = []


    def crawl(self):
        downloader = Downloader(self.starting_url)
        app = downloader.get_app_from_link()


        self.apps.append(app)
        self.depth_links.append(app.links)

        links_visited = set()

        while self.current_depth < self.depth:
             current_links = []
             for link in self.depth_links[self.current_depth]:
                 if link not in links_visited:
                    current_app = Downloader(link).get_app_from_link()
                    current_links.extend(current_app.links)
                    with open(str('./resources/jsonFiles/' + current_app.uid + '_tiem_pipeline.txt'), 'w') as outfile:
                        json.dump(current_app.__dict__, outfile)
                    self.apps.append(current_app)
                 links_visited.add(link)
             self.current_depth += 1
             self.depth_links.append(current_links)


        for app in self.apps:
            searcher.es.index(index='researchGate', doc_type='articles', body=current_app.__dict__)
            print('this app is crawled:    ' + app)