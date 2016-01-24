from crawler.scheduler import Scheduler

# link = 'https://www.researchgate.net/publication/278332447_MCMC_for_Variationally_Sparse_Gaussian_Processes'


# crawler = Scheduler(link, 0)
# crawler.crawl()
from kmeans.kmeans import Kmeans
kmeans = Kmeans(
    vectors=[
        [1, 1, 1, 0],
        [0, 2, 1, 0],
        [1, 1, 0, 1],
        [2, 0, 0, 1]])
kmeans.kmenas()
