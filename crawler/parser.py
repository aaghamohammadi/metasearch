from bs4 import BeautifulSoup


class Parser:
    def __init__(self, start_page):
        self.start_page = start_page

    def parse(self):
        soup = BeautifulSoup(self.start_page.text, 'lxml')
        for title in soup.select("h1.publication-title"):
            print(title.text)
