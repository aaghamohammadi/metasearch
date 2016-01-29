from crawler.scheduler import Scheduler
from kmeans.kmeans import Kmeans


link = 'http://www.researchgate.net/publication/278332447_MCMC_for_Variationally_Sparse_Gaussian_Processes'

crawler = Scheduler(link, 20)
crawler.crawl()


"""kmeans = Kmeans(
    vectors=[
        [1, 1, 1, 0],
        [0, 2, 1, 0],
        [1, 1, 0, 1],
        [2, 0, 0, 1]])
kmeans.kmenas()
"""