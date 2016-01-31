from crawler.scheduler import Scheduler
from kmeans.kmeans import Kmeans


link = 'http://www.researchgate.net/publication/278332447_MCMC_for_Variationally_Sparse_Gaussian_Processes'

crawler = Scheduler()
crawler.crawl()
"""
from sklearn.feature_extraction.text import CountVectorizer

documents = (
    "The sky is blue",
    "The sun is bright",
    "The sun in the sky is bright",
    "We can see the shining sun, the bright sun"
)
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(documents).todense()
vectors=vectors.tolist()
print(vectors)
# vectors = [
#     [1, 1, 1, 0],
#     [0, 2, 1, 0],
#     [1, 1, 0, 1],
#     [2, 0, 0, 1]]
# print(vectors)

kmeans = Kmeans(vectors)
kmeans.kmenas()
"""