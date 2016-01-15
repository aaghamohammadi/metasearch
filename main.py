
from crawler.scheduler import Scheduler

link = 'https://www.researchgate.net/publication/278332447_MCMC_for_Variationally_Sparse_Gaussian_Processes'


crawler = Scheduler(link, 0)
crawler.crawl()
