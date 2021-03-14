import numpy as np

def cumsum(a):
    #param A: np.array[m,n]
    #YOUR CODE
    a = np.array(a)
    a = a.cumsum(axis=1)
    result = a
    return result