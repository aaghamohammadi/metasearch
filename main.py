# from bs4 import BeautifulSoup
# import requests
#
# r = requests.get('http://google.com')
# soup = BeautifulSoup(r.text, 'lxml')
#
# print(soup.prettify())
from crawler.scheduler import Scheduler

crawler = Scheduler('http://www.researchgate.net/researcher/8159937_Zoubin_Ghahramani', 0)
crawler.crawl()
