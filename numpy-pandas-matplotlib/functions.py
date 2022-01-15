from typing import List
import math
import numpy as np
import pickle


def prod_non_zero_diag(X: List[List[int]]) -> int:
    c: int = 0
    product: int = 1
    zero_check: int = 0
    for i in X:
        if c == len(i):
            break
        if i[c] != 0:
            product *= i[c]
        else:
            zero_check += 1
        c += 1

    if zero_check == c:
        return -1
    else:
        return product
    pass


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    x.sort()
    y.sort()
    return x == y
    pass


def max_after_zero(x: List[int]) -> int:
    y = []
    c = 0
    for i in x:
        if c != len(x) - 1 and i == 0:
            y.append(x[c + 1])
        c += 1

    if len(y) == 0:
        return -1
    else:
        return sorted(y, reverse=True)[0]
    pass


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    ret = []
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
        ret.append(tmp)
    return ret
    pass


def run_length_encoding(x: List[int]) -> (List[int], List[int]):
    run = [x[0]]
    length = [0]
    for i in x:
        if run[len(run) - 1] != i:
            run.append(i)
            length.append(1)
        else:
            length[len(run) - 1] += 1

    return run, length
    pass


def pairwise_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    t = []
    for i in X:
        vec = []
        for j in Y:
            s = 0
            p = [(x1 - x2) ** 2 for (x1, x2) in zip(i, j)]
            for k in p:
                s += k
            vec.append(math.sqrt(s))
        t.append(vec)
    return t


pass
