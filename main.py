from crawler.scheduler import Scheduler
from kmeans.kmeans import Kmeans
import matplotlib.pyplot as plt

# link = 'http://www.researchgate.net/publication/278332447_MCMC_for_Variationally_Sparse_Gaussian_Processes'
#
# crawler = Scheduler(link, 20)
# crawler.crawl()

from sklearn.feature_extraction.text import CountVectorizer

documents = (
    "The sky is blue",
    "The sun is bright",
    "The sun in the sky is bright",
    "We can see the shining sun, the bright sun"
)
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(documents).todense().tolist()

kmeans = Kmeans(vectors)
k_points = []
j_points = []
for i in range(len(vectors)):
    k_points.append(i + 1)
    j_points.append(kmeans.kmenas(i + 1))

# print(k_points)
# print(j_points)
plt.plot(j_points, k_points)
plt.show()
