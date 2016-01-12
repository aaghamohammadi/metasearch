from crawler.downloader import Downloader


class Scheduler:
    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        depth = 0  # TODO
        pass

    def crawl(self):
        downloader = Downloader(self.starting_url)
        downloader.get_app_from_link()
        pass
