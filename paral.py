# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:44:48 2015

@author: adalsteinn
"""
import cPickle as pickle
from scipy.sparse import *
from scipy import *
import numpy as np
import time
import multiprocessing as mp
from multiprocessing import freeze_support
import random
import string
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


# Define an output queue
output = mp.Queue()



def split_calculator(lenY):
    split = lenY/6
    splits = []
    for i in range(6):
        splits.append(i*split)
    splits.append(lenY)
    return splits
        
a = split_calculator(10000)
    
Y = Y3
splitlist = split_calculator(shape(Y)[0])
eps = 0.15

def paralleller(Y, splitlist, eps, output):
    freeze_support()
    # Setup a list of processes that we want to run
    processes = [mp.Process(target=querycalculate.calculate_neightbours, args=(Y,splitlist[0],splitlist[1],eps, output,1)),
                 mp.Process(target=querycalculate.calculate_neightbours, args=(Y,splitlist[1],splitlist[2],eps, output,2)),
                 mp.Process(target=querycalculate.calculate_neightbours, args=(Y,splitlist[2],splitlist[3],eps, output,3)),
                 mp.Process(target=querycalculate.calculate_neightbours, args=(Y,splitlist[3],splitlist[4],eps, output,4)),
                 mp.Process(target=querycalculate.calculate_neightbours, args=(Y,splitlist[4],splitlist[5],eps, output,5)),
                 mp.Process(target=querycalculate.calculate_neightbours, args=(Y,splitlist[5],splitlist[6],eps, output,6))]
    
    # Run processes
    for p in processes:
        p.start()
    
    print 'process done'
    print processes
    
    # Exit the completed processes
    for p in processes:
        p.join()
        
    print 'joining done'
    print processes
    
    # Get process results from the output queue
    results = [output.get() for p in processes]

    return results


start = time.time()
#a = paralleller(Y, splitlist, eps, output)

a = querycalculate.calculate_neightbours1(Y,splitlist[0],splitlist[6],eps,1)
stop = time.time()
elapsed = stop - start
elapsed



