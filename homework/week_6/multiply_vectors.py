import numpy as np


# Test cases:
# 1)
# [1, 2, 3]
# [-1, -2, -3]
# Result:
# 1) -14

def no_numpy_scalar(v1, v2):
    # param v1, v2: lists of 3 ints
    # YOUR CODE: please do not use numpy

    result = 0
    n = len(v1)
    for i in range(n):
        result += v1[i] * v2[i]

    return result


def numpy_scalar(v1, v2):
    # param v1, v2: np.arrays[3]
    # YOUR CODE
    v1 = np.array(v1)
    v2 = np.array(v2)
    result = v1.dot(v2)
    return result
