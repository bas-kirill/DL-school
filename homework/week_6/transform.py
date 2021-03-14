import numpy as np


def transform(x, a=1):
    """
    param X: np.array[batch_size, n]
    """
    n = len(x)
    x = np.array(x)
    result = []
    for i in range(n):
        if i % 2 == 1:
            result.append(a)
        else:
            result.append(x[i]**3)

    result.reverse()
    result = np.concatenate((x, result))
    return result.tolist()