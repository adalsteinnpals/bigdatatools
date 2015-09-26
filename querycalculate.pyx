#cython: boundscheck=False
#cython: wraparound=False
#cython: cdivision=True
#cython: nonecheck=False

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
cimport numpy as np

ctypedef np.int32_t cINT32
ctypedef np.double_t cDOUBLE

def print_sparse(m):
    cdef np.ndarray[cINT32, ndim=1] row, col
    cdef np.ndarray[cDOUBLE, ndim=1] data
    cdef int i
    if not isinstance(m, coo_matrix):
        m = coo_matrix(m)
    row = m.row.astype(np.int32)
    col = m.col.astype(np.int32)
    data = m.data.astype(np.int32)
    for i in range(np.shape(data)[0]):
        print row[i], col[i], data[i]
        

def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )
        
ctypedef np.float32_t DTYPE_t

def calculate_neightbours(m,point,start,stop,eps,output,pos):
    cdef np.ndarray[cINT32, ndim=1] indices, indptr, posj, posi
    neighbours = []
    cdef int i, j, c1, c2
    if not isinstance(m, csr_matrix):
        m = csr_matrix(m)
    indices = m.indices.astype(np.int32)
    indptr = m.indptr.astype(np.int32)
    for j in xrange(start,stop):
        posi = indices[indptr[point]:indptr[point+1]]
        posj = indices[indptr[j]:indptr[j+1]]
        inters = set(posi).intersection(posj)
        Jlen = 1.0-float(len(inters))/(len(posi)+len(posj)-len(inters))
        if Jlen<=eps:
            neighbours.append(j)
    neighbours = np.asarray(neighbours).astype(int)
    output.put(neighbours)
    
def calculate_neightbours1(m,start,stop,eps,pos):
    cdef np.ndarray[cINT32, ndim=1] indices, indptr, posj, posi
    nindices = []
    nindptr = []
    result = []
    cdef int i, j, c1, c2
    if not isinstance(m, csr_matrix):
        m = csr_matrix(m)
    indices = m.indices.astype(np.int32)
    indptr = m.indptr.astype(np.int32)
    c = 0
    for i in xrange(start,stop): #calculate neighbours of every actor
        for j in xrange(np.shape(indptr)[0]-1):
            posi = indices[indptr[i]:indptr[i+1]]
            posj = indices[indptr[j]:indptr[j+1]]
            inters = list([1,2,3])
            #inters = set(posi).intersection(posj)
            Jlen = 1.0-float(len(inters))/(len(posi)+len(posj)-len(inters))
            if Jlen<=eps:
                nindices.append(j)
                c = c+1
        nindptr.append(c)
    result.append(pos)
    result = list([pos]) + list([len(nindptr)]) + nindptr + nindices
    result = np.asarray(result).astype(int)
    return result
        
def print_csr(m):
    cdef np.ndarray[cINT32, ndim=1] indices, indptr
    cdef np.ndarray[cDOUBLE, ndim=1] data
    cdef int i
    if not isinstance(m, csr_matrix):
        m = csr_matrix(m)
    indices = m.indices.astype(np.int32)
    indptr = m.indptr.astype(np.int32)
    data = m.data.astype(np.float64)
    for i in range(np.shape(indptr)[0]-1):
        for j in range(indptr[i], indptr[i+1]):
            print i, indices[j], data[j]
    return indptr
    
def csr_get_indptr(m):
    cdef np.ndarray[cINT32, ndim=1] indices, indptr
    cdef np.ndarray[cDOUBLE, ndim=1] data
    if not isinstance(m, csr_matrix):
        m = csr_matrix(m)
    indptr = m.indptr.astype(np.int32)
    return indptr
    
def csr_get_indices(m):
    cdef np.ndarray[cINT32, ndim=1] indices, indptr
    cdef np.ndarray[cDOUBLE, ndim=1] data
    if not isinstance(m, csr_matrix):
        m = csr_matrix(m)
    indices = m.indices.astype(np.int32)
    return indices

"""
from scipy.sparse import *
from scipy import *
import numpy as np
cimport numpy as np


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
    
    
def Jlen1(Y):
    a=[]
    for i in range(shape(Y)[0]-1):
        indices1 = Y[i].indices
        indices2 = Y[i+1].indices
        inters = set(indices1).intersection(indices2)
        a.append(inters)
    return a
    
def Jlen3(Y):
    a=[]
    for i in range(shape(Y)[0]-1):
        a.append(i)
    return a """