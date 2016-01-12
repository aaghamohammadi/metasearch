import requests


class Downloader:
    def get_app_from_link(self, link):
        start_page = requests.get(link)

        print(start_page.text)
