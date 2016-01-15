from crawler.downloader import Downloader


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

        # in hamin joori ta depth moshakhasi ke bala taiien shode download mikone. link haie tekrari ro darnaza nemigire baiad khodet chek koni

        # self.apps.append(app)
        # self.depth_links.append(app.links)
        #
        # while self.current_depth < self.depth:
        #     current_links = []
        #     for link in self.depth_links[self.current_depth]:
        #         current_app = Downloader(link).get_app_from_link()
        #         current_links.extend(current_app.links)
        #         self.apps.append(current_app)
        #     self.current_depth += 1
        #     self.depth_links.append(current_links)
