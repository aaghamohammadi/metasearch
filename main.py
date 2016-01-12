# from bs4 import BeautifulSoup
# import requests
#
# r = requests.get('http://google.com')
# soup = BeautifulSoup(r.text, 'lxml')
#
# print(soup.prettify())
from crawler.scheduler import Scheduler

crawler = Scheduler(
    'https://www.researchgate.net/publication/273488773_Variational_Infinite_Hidden_Conditional_Random_Fields', 0)
crawler.crawl()
