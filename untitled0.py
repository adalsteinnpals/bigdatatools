# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:11:16 2015

@author: adalsteinn
"""

from scipy.sparse import *
from scipy import *
import numpy as np





def Jlen(par1, par2, Y):
    indices1 = Y[par1].indices
    indices2 = Y[par2].indices
    inters = set(indices1).intersection(indices2)
    Jlen = 1.0-float(len(inters))/(len(indices1)+len(indices2)-len(inters))
    return Jlen

def regionQueryall(Y, eps):
    lenY = shape(Y)[0]
    Yneighbours = identity(lenY, dtype='int8')
    for P in range(lenY-1): # AAATHHHHH
        for P1 in range(lenY-P):
            P2 = P+P1
            Jlength = Jlen(P,P2, Y)
            if Jlength <= eps:
                Yneighbours[P,P2] = 1
    return Yneighbours
    
    
    
    
    
    
def timelooper(N):
    for i in range(N):
        indices1 = Y[i].indices
    return
    

Y = Y5
t1 = time.time()
timelooper(100000)
t2 = time.time()
elapsed = t2 - t1
elapsed