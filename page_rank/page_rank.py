import numpy as np
from scipy.sparse import csc_matrix

def pageRank(GT, s = .85, maxerr = .001, threshold = 0):
    G = GT[0]

    n = G.shape[0]

    # transform G into markov matrix M
    M = csc_matrix(G,dtype=np.float)
    rsums = np.array(M.sum(1))[:,0]
    ri, ci = M.nonzero()
    M.data /= rsums[ri]

    # bool array of sink states
    sink = rsums==0

    # Compute pagerank r until we converge
    ro, r = np.zeros(n), np.ones(n)
    count = -1
    while np.sum(np.abs(r-ro)) > maxerr and count < threshold:
        ro = r.copy()
        # calculate each pagerank at a time
        for i in xrange(0,n):
            # inlinks of state i
            Ii = np.array(M[:,i].todense())[:,0]
            # account for sink states
            Si = sink / float(n)
            # account for teleportation to state i
            Ti = np.ones(n) / float(n)

            r[i] = ro.dot( Ii*s + Si*s + Ti*(1-s) )
        if threshold != 0:
            count += 1
    # return normalized pagerank
    return (r/sum(r), GT[1])




