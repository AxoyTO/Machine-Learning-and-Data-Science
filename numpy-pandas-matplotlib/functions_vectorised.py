import numpy
import numpy as np
import pickle
from itertools import groupby


def prod_non_zero_diag(X: np.ndarray) -> int:
    if not 0 in X.diagonal():
        return X.diagonal().prod()
    if len(X.diagonal().nonzero()[0]) == 0:
        return -1
    else:
        prod = 1
        for i in X[X.diagonal().nonzero(), X.diagonal().nonzero()]:
            for j in i:
                prod *= j
            break
        return prod
    pass


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    """
    Return True if both 1-d arrays create equal multisets, False if not.
    Return type: bool / np.bool_
    """
    x.sort()
    y.sort()
    return True if False not in (x == y) else False
    pass


def max_after_zero(x: np.ndarray) -> int:
    y = np.where(x == 0)[0] + 1
    if y.size == 0:
        return -1
    elif y.size == 1 and y == x.size:
        return -1
    maximum = 0
    for i in y:
        if x[i] > maximum:
            maximum = x[i]
    return maximum
    pass


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """
    #TOO SLOW
    ret = [[]] * len(image)
    v = 0
    for i in image:
        tmp = []
        for j in i:
            c = 0
            t = 0
            for k in j:
                if c == len(j):
                    break
                t += k * weights[c]
                c += 1
            tmp.append(t)
        ret[v] = tmp
        v += 1
    return ret
    #----------
    #EVEN SLOWER
    ret = numpy.zeros(shape=(len(image), len(image)))
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            t = 0
            for k in range(0, len(image[i][j])):
                t += weights[k] * image[i][j][k]
            ret[i][j] = t
    return ret
    """
    ret = np.dot(image, weights)
    return ret
    pass


def run_length_encoding(x: np.ndarray) -> (np.ndarray, np.ndarray):
    if x.ndim != 1:
        return -1
    n = x.size

    if n == 0:
        return -1

    else:
        loc_run_start = np.empty(n, dtype=bool)
        loc_run_start[0] = True
        np.not_equal(x[:-1], x[1:], out=loc_run_start[1:])
        run_starts = np.nonzero(loc_run_start)[0]
        run_values = x[loc_run_start]

        run_lengths = np.diff(np.append(run_starts, n))

        return run_values, run_lengths


def pairwise_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    Z = np.linalg.norm(X[:, None, :] - Y[None, :, :], ord=None, axis=-1)
    return Z
    pass
