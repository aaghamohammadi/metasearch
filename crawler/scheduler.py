from crawler.downloader import Downloader
from elasticSearch import searcher
import json
import global_functions

class Scheduler:
    def __init__(self, starting_url, num):
        self.starting_url = starting_url
        self.depth = num
        self.num_docs_crawled = 0
        self.current_depth = 0
        self.depth_links = []
        self.apps = []


    def crawl(self):
        downloader = Downloader(self.starting_url)
        app = downloader.get_app_from_link()


        self.apps.append(app)
        self.depth_links.append(app.links)

        links_visited = set()

        while self.num_docs_crawled < self.depth:
             current_links = []
             for link in self.depth_links[self.current_depth]:
                 if link not in links_visited:
                    current_app = Downloader(link).get_app_from_link()
                    current_links.extend(current_app.links)
                    with open(str('./resources/jsonFiles/' + 'item_pipeline_' + str(self.num_docs_crawled) + '_' + current_app.uid + '.txt'), 'w') as outfile:
                        json.dump(current_app.__dict__, outfile)

                    self.num_docs_crawled += 1
                    self.apps.append(current_app)
                 links_visited.add(link)
             self.current_depth += 1
             self.depth_links.append(current_links)

