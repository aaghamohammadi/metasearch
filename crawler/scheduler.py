from crawler.downloader import Downloader
import json
from global_functions import update_progress

l_default = 'http://www.researchgate.net/publication/278332447_MCMC_for_Variationally_Sparse_Gaussian_Processes'

class Scheduler:
    def __init__(self, starting_urls=[l_default], num=1000, in_degree=10, out_degree=10):
        self.starting_urls = starting_urls
        self.num_docs_to_be_crawled = num
        self.num_docs_crawled = 0
        self.current_depth = 0
        self.depth_links = []
        self.depth_out_links = []
        self.apps = []
        self.in_degree = in_degree
        self.out_degree = out_degree
        self.links_visited = set()


    def crawl(self):
        for start_link in self.starting_urls:
            downloader = Downloader(start_link)
            app = downloader.get_app_from_link()

            self.links_visited.add(start_link)

            self.apps.append(app)
            self.depth_links.append(app.in_links)
            self.depth_links.append(app.out_links)
            with open(str('./resources/jsonFiles/' + 'item_pipeline_' + 0 + '_' + app.uid + '.json'), 'w') as outfile:
                json.dump(app.__dict__, outfile)
            self.num_docs_crawled = 1

        while self.num_docs_crawled < self.num_docs_to_be_crawled:
            current_in_links = []
            current_out_links = []

            count = 0
            for link in self.depth_links[self.current_depth]:


                if link not in self.links_visited and count < self.in_degree :
                    current_app = Downloader(link).get_app_from_link()
                    if current_app is 0:
                        continue
                    current_in_links.extend(current_app.in_links)
                    current_out_links.extend(current_app.out_links)
                    with open(str('./resources/jsonFiles/' + 'item_pipeline_' + str(self.num_docs_crawled) + '_' + current_app.uid + '.json'), 'w') as outfile:
                        json.dump(current_app.__dict__, outfile)
                    update_progress(self.num_docs_crawled, self.num_docs_to_be_crawled)
                    self.num_docs_crawled += 1
                    self.apps.append(current_app)
                    self.links_visited.add(link)
                    count += 1



            self.depth_links.append(current_in_links)
            self.depth_links.append(current_out_links)
            self.current_depth += 1

            current_in_links = []
            current_out_links = []

            count = 0
            for link in self.depth_links[self.current_depth]:
                if link not in self.links_visited and count < self.out_degree:
                    current_app = Downloader(link).get_app_from_link()
                    if current_app is 0:
                        continue
                    current_in_links.extend(current_app.in_links)
                    current_out_links.extend(current_app.out_links)
                    with open(str('./resources/jsonFiles/' + 'item_pipeline_' + str(self.num_docs_crawled) + '_' + current_app.uid + '.json'), 'w') as outfile:
                        json.dump(current_app.__dict__, outfile)
                    update_progress(self.num_docs_crawled, self.num_docs_to_be_crawled)
                    self.num_docs_crawled += 1
                    self.apps.append(current_app)
                    self.links_visited.add(link)
                    count += 1


            self.current_depth += 1
            self.depth_links.append(current_in_links)
            self.depth_links.append(current_out_links)


"""
        while self.num_docs_crawled < self.num_docs_to_be_crawled:
            current_links = []

            count = 0
            for link in self.depth_links[self.current_depth]:

                if link not in self.links_visited and count < self.in_degree :
                    current_app = Downloader(link).get_app_from_link()
                    if current_app is 0:
                        continue
                    current_links.extend(current_app.in_links)
                    with open(str('./resources/jsonFiles/' + 'item_pipeline_' + str(self.num_docs_crawled) + '_' + current_app.uid + '.txt'), 'w') as outfile:
                        json.dump(current_app.__dict__, outfile)
                    update_progress(self.num_docs_crawled, self.num_docs_to_be_crawled)
                    self.num_docs_crawled += 1
                    self.apps.append(current_app)
                    self.links_visited.add(link)
                    count += 1


            self.depth_links.append(current_links)
            self.current_depth += 1

            current_links = []
            count = 0
            for link in self.depth_links[self.current_depth]:
                if link not in self.links_visited and count < self.out_degree:
                    current_app = Downloader(link).get_app_from_link()
                    if current_app is 0:
                        continue
                    current_links.extend(current_app.out_links)
                    with open(str('./resources/jsonFiles/' + 'item_pipeline_' + str(self.num_docs_crawled) + '_' + current_app.uid + '.txt'), 'w') as outfile:
                        json.dump(current_app.__dict__, outfile)
                    update_progress(self.num_docs_crawled, self.num_docs_to_be_crawled)
                    self.num_docs_crawled += 1
                    self.apps.append(current_app)
                    self.links_visited.add(link)
                    count += 1


            self.current_depth += 1
            self.depth_links.append(current_links)
"""

