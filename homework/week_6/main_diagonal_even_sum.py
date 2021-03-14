import numpy as np #не стирать!        


def diag_2k(a):
    #param a: np.array[size, size]
    #YOUR CODE
    a = np.array(a)
    diag = a.diagonal()
    diag = diag[diag % 2 == 0]
    result = diag.sum()
    return result