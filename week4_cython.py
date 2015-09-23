# -*- coding: utf-8 -*-

import cPickle as pickle
from scipy.sparse import *
from scipy import *
import numpy as np
import time
import querycalculate


X1 = pickle.load(open('data_10points_10dims.dat', 'r'))
X2 = pickle.load(open('data_100points_100dims.dat', 'r'))
X3 = pickle.load(open('data_1000points_1000dims.dat', 'r'))
X4 = pickle.load(open('data_10000points_10000dims.dat', 'r'))
X5 = pickle.load(open('data_100000points_100000dims.dat', 'r'))


Y1 = csr_matrix(X1)
Y2 = csr_matrix(X2)
Y3 = csr_matrix(X3)
Y4 = csr_matrix(X4)
Y5 = csr_matrix(X5)




def expandCluster(P, neighbours, C, eps, M, checked):
    cluster[P] = C
    while True:
        uncheckedneighbours = list(set(neighbours) - set(set(checked).intersection(neighbours)))
        if len(uncheckedneighbours) == 0:
            break
        P = uncheckedneighbours[0]
        checked.append(P)
        neighboursm = Yn[P].indices
        if len(neighboursm) >= M:
            neighbours = list(neighbours) + list(set(neighboursm) - set(neighbours))
        cluster[P] = C
        
                
        
    
# Main run


Y = Y3
cluster = {}
checked = []
lenY = shape(Y)[0]
C = 0
M = 2
eps = 0.15
t1 = time.time()
Ytemp = query.regionQueryall(Y,eps) # AAATTTHHHH
t2 = time.time()
Yn = Ytemp + Ytemp.transpose()- identity(lenY, dtype = 'int8')
Yn = csr_matrix(Yn)
while True:
    Pleft = list(set(range(lenY)) - set(set(checked).intersection(range(lenY))))
    if len(Pleft) == 0:
        t3 = time.time()
        break
    P = Pleft[0]
    checked.append(P)
    neighbours = Yn[P].indices
    if len(neighbours) < M:
        cluster[P] = -1
    else:
        C = C + 1
        expandCluster(P, neighbours, C, eps,M, checked)
        

time1 = t2-t1
time2 = t3-t2



import querycalculate
start = time.time()
a = querycalculate.print_csr(Y5)
stop = time.time()
elapsed = stop - start
elapsed

max(cluster.values())
        

    
        