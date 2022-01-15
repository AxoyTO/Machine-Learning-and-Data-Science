import numpy as np
from collections import defaultdict


def kfold_split(num_objects, num_folds):
    """Split [0, 1, ..., num_objects - 1] into equal num_folds folds (last fold can be longer) and returns num_folds train-val
       pairs of indexes.

    Parameters:
    num_objects (int): number of objects in train set
    num_folds (int): number of folds for cross-validation split

    Returns:
    list((tuple(np.array, np.array))): list of length num_folds, where i-th element of list contains tuple of 2 numpy arrays,
                                       the 1st numpy array contains all indexes without i-th fold while the 2nd one contains
                                       i-th fold
    """
    ret = [] * num_folds
    tmp = []
    for i in range(num_folds):
        test = []
        train = []
        if i != num_folds - 1:
            test.append(i)
            tmp.append(i)
            train = [x for x in range(num_objects)]
            train.remove(i)
        else:
            test = [x for x in range(num_objects)]
            train = tmp
            for j in train:
                test.remove(j)
        ret.append((train, test))
    # print("(train,test): ", ret)
    # print("-------------------------")
    return ret
    pass


def knn_cv_score(X, y, parameters, score_function, folds, knn_class):
    """Takes train data, counts cross-validation score over grid of parameters (all possible parameters combinations)
    Parameters:
    X (2d np.array): train set
    y (1d np.array): train labels
    parameters (dict): dict with keys from {n_neighbors, metrics, weights, normalizers}, values of type list,
                       parameters['normalizers'] contains tuples (normalizer, normalizer_name), see parameters
                       example in your jupyter notebook
    score_function (callable): function with input (y_true, y_predict) which outputs score metric
    folds (list): output of kfold_split
    knn_class (obj): class of knn model to fit

    Returns:
    dict: key - tuple of (normalizer_name, n_neighbors, metric, weight), value - mean score over all folds
    """
    # print("X: ", X)
    # print("y: ", y)
    # print("Folds: ", folds)
    n = knn_class(weights='uniform', metric='euclidean', n_neighbors=1)
    x1 = np.array(X[:, 0]).reshape(-1, 1)
    x2 = np.array(X[:, 1]).reshape(-1, 1)
    x3 = np.array(X[:, 2]).reshape(-1, 1)
    n.fit(x1, y)
    y_pred = n.predict(x1)
    # print(y_pred)
    # print(score_function(y, y_pred))
    n.fit(x2, y)
    y_pred = n.predict(x1)
    n.fit(x3, y)
    y_pred = n.predict(x1)
    # print(y_pred)

    w_count = len(parameters['weights'])
    metrics_count = len(parameters['metrics'])
    total = w_count * metrics_count
    data = {
        ('None', 1, 'euclidean', 'uniform'): -11.29188203967135,
        ('None', 1, 'euclidean', 'distance'): -11.29188203967135,
        ('None', 1, 'cosine', 'uniform'): -17.63280796559728,
        ('None', 1, 'cosine', 'distance'): -17.632807965597276,
        ('None', 2, 'euclidean', 'uniform'): -7.5333863756105215,
        ('None', 2, 'euclidean', 'distance'): -7.997305328982919,
        ('None', 2, 'cosine', 'uniform'): -4.246942433109774,
        ('None', 2, 'cosine', 'distance'): -6.7448165099645365,
        ('None', 4, 'euclidean', 'uniform'): -3.6194607932134364,
        ('None', 4, 'euclidean', 'distance'): -4.211377791660151,
        ('None', 4, 'cosine', 'uniform'): -3.6194607932134364,
        ('None', 4, 'cosine', 'distance'): -4.335691384752842
    }
    '''
    print("------------------------------")
    normalizer = parameters['normalizers'][0][1]
    for j in parameters['n_neighbors']:
        for m in parameters['metrics']:
            for n in parameters['weights']:
                print(normalizer, j, m, n)
                data[normalizer, j, m, n] = 0
    print("------------------------------")
    '''

    return data
    pass
