import numpy as np

# Test cases:
# 1)
# a = [[5, 1, -2, 0], [0, 3, 4, 3], [2, 3, 1, 1]]
# b = [[1, -3], [2, -2], [3, -1], [0, 0]]
# Result:
# 1) [[1, -15], [18, -10], [11, -13]]

def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param first: list of "size" lists, each contains "size" floats
    """

    n, l, m = len(first), len(first[0]), len(second[0])
    result = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            sum = 0
            for k in range(l):
                sum += first[i][k] * second[k][j]
            result[i][j] = sum
    return result


def numpy_mult(first, second):
    """
    param first: np.array[size, size]
    param second: np.array[size, size]
    """

    np_a = np.array(first)
    np_b = np.array(second)

    result = np_a.dot(np_b).tolist()
    return result
