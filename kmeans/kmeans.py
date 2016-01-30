from math import sqrt
from operator import itemgetter
import numpy
from global_functions import update_progress


class Kmeans:
    def __init__(self, vectors):
        self.vectors = vectors

    @staticmethod
    def size(u):

        return sqrt(sum(map(lambda x: x * x, u)))

    @staticmethod
    def dot_product(u, v):
        return sum(map(lambda x: x[0] * x[1], zip(u, v)))

    def similarity(self, u, v):
        return 1.0 * self.dot_product(u, v) / (self.size(u) * self.size(v))

    @staticmethod
    def sum_of_vector(vec_list):
        vsum = [0 for x in range(len(vec_list[0]))]
        for vec in vec_list:
            vsum = [s + x for s, x in zip(vsum, vec)]
        return vsum

    def average_of_vectors(self, vec_list):
        return list(map(lambda x: x / len(vec_list), self.sum_of_vector(vec_list)))

    def belongs_to_cluster(self, v, centeroids):
        similarities = [self.similarity(u, v) for u in centeroids]
        # print('similarities for', v, '=', similarities)
        return max(enumerate(similarities), key=itemgetter(1))[0]

    def kmenas(self, k):
        j = 0
        centeroids = []
        for i in range(k):
            centeroids.append(self.vectors[i])
        # centeroids = [self.vectors[0], self.vectors[1]]
        iterations = 5
        # k = len(centeroids)
        for iterate in range(iterations):
            update_progress(iterate, iterations)
            cluster_members = [[] for u in centeroids]

            for v in self.vectors:
                cluster_members[self.belongs_to_cluster(v, centeroids)].append(v)

                # for clnum in range(k):
                #     print('members of cluster', clnum, ' = ', cluster_members[clnum])
                #     print(len(cluster_members[clnum]))

            for i in range(k):
                centeroids[i] = self.average_of_vectors(cluster_members[i])
                labels = [self.similarity(u, centeroids[i]) for u in cluster_members[i]]
                print("labels for cluster ", i, ": ", cluster_members[i][labels.index(max(labels))])

                for temp in cluster_members[i]:
                    j += sum(map(lambda x: (x[0] - x[1]) ** 2, zip(temp, centeroids[i])))

        return j
