# -*- coding: utf-8 -*-

import cPickle as pickle
from scipy.sparse import *
from scipy import *
import numpy as np
import time

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

def Jlen(par1, par2):
    indices1 = Y[par1].indices
    indices2 = Y[par2].indices
    inters = set(indices1).intersection(indices2)
    Jlen = 1.0-float(len(inters))/(len(indices1)+len(indices2)-len(inters))
    return Jlen


def regionQueryall(par1, lenY, eps):
    neighbours = [par1]
    others = allbutone(par1,lenY)
    for i in range(len(others)):
        Jlength = Jlen(par1,others[i])
        if Jlength <= eps:
            neighbours.append(others[i])
    return neighbours
            


def allbutone(par1, lenY):
    arr = range(lenY)
    newarr = arr[:par1]+arr[(par1+1):]
    return newarr


def expandCluster(P, neighbours, C, eps, M, checked):
    cluster[P] = C
    while True:
        uncheckedneighbours = list(set(neighbours) - set(set(checked).intersection(neighbours)))
        if len(uncheckedneighbours) == 0:
            break
        P = uncheckedneighbours[0]
        checked.append(P)
        neighboursm = regionQuery(P, lenY, eps)
        if len(neighboursm) >= M:
            neighbours = neighbours + list(set(neighboursm) - set(neighbours))
        cluster[P] = C
        
                
        
    
# Main run

timer = []
Y = Y1
cluster = {}
checked = []
lenY = shape(Y)[0]
C = 0
M = 2
eps = 0.4
while True:
    Pleft = list(set(range(lenY)) - set(set(checked).intersection(range(lenY))))
    if len(Pleft) == 0:
        break
    P = Pleft[0]
    checked.append(P)
    neighbours = regionQuery(P, lenY, eps)
    if len(neighbours) < M:
        cluster[P] = -1
    else:
        C = C + 1
        expandCluster(P, neighbours, C, eps,M, checked)



max(cluster.values())


start = time.time()
a = query.regionQueryall(Y3,0.15)
stop = time.time()
elapsed = stop - start
elapsed

max(cluster.values())
        
        
        
def Jlen(par1, par2, Y):
    indices1 = Y[par1].indices
    indices2 = Y[par2].indices
    inters = set(indices1).intersection(indices2)
    Jlen = 1.0-float(len(inters))/(len(indices1)+len(indices2)-len(inters))
    return Jlen
    
from joblib import Parallel, delayed        

def regionQueryall(Y, eps):
    lenY = shape(Y)[0]
    Yneighbours = identity(lenY, dtype='int8')
    for P in range(lenY-1):
        for P1 in range(lenY-P):
            P2 = P+P1
            Jlength = Jlen(P,P2, Y)
            if Jlength <= eps:
                Yneighbours[P,P2] = 1
    return Yneighbours
    

a = regionQueryall(Y1,0.4)
    





Y = Y5
a = []
for i in range(shape(Y)[0]):
    a.append(len(Y[i].indices))
        