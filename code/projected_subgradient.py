# A implementation of Projected Subgradient Decent
# created by Guoqing Zhang 2019.7.14

import numpy as np
from numpy.linalg import inv
import datetime
import matplotlib.pyplot as plt
# Use T and tildeX to compute projection
def computeProjection(A,y):
    I = np.identity(A.shape[1])
    I = np.mat(I)
    A = np.mat(A)
    y = np.mat(y)
    temp =  A.transpose() *inv(A * A.transpose())
    T = I -temp*A
    tildeX = temp*y
    return [T,tildeX]
def randomSequenceNoRepeat(k,n):
    r = list(range(0,n))
    
    for i in range(k):
        j = np.random.random_integers(0,n-1)
        #print(j)
        r[i],r[j] = r[j],r[i]
    return r[:k]
# k means the sparsity, m, n is the dimension of matrix A
def randomGeneratexAy(k,m,n):
    A =  np.random.randn(m,n)
    x = np.random.rand(n)
    A = np.mat(A)
    x = np.mat(x).transpose()
    zero_indice = randomSequenceNoRepeat(n-k,n)
    for i in zero_indice:
        x[i] = 0
    y = A*x 
    return x,A,y
# recoverX
def recoverX(A,y):
    T,tildeX = computeProjection(A,y)
    x = np.zeros(A.shape[1])
    x = np.mat(x).transpose()
    
    for i in range(1,100000):
        #print(i,"iteration...")
        x = tildeX + T*(x - 1/i * np.sign(x))
    return x
def drawResult(sf):
    x = list(range(0,len(sf)))
    plt.plot(x,sf)
    plt.show()

if __name__ == "__main__":
    m = 200
    n = 500
    frac = [0 for i in range(501)]
    last = 500
    for i in range(50):
        frac[i] = 1.0
    
    for k in range(50,501):
        success = 0
        for i in range(60):
            #starttime = datetime.datetime.now()
            x,A,y = randomGeneratexAy(k,m,n)
            #print(x)
            hatX = recoverX(A,y)
            hatX = hatX - x
            hatX = np.fabs(hatX)
            hatX[hatX<0.01] = 0 
            hatX[hatX!=0] = 1   
            #endtime = datetime.datetime.now()
            #print((endtime - starttime).microseconds/1000.0)
            if np.sum(hatX) == 0.0:
                success = success + 1
        frac[k] = success/60
        print(k,success/60)
        if(frac[k] == 0.0):
            last = k
            break
    for i in range(last,501):
        frac[k] = 0.0
    frac[0] = 0.0
    drawResult(frac)
    