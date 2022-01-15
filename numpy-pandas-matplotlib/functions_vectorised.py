import numpy as np
import pickle


def prod_non_zero_diag(X: np.ndarray) -> int:
    """
    Compute product of nonzero elements from matrix diagonal,
    return -1 if there is no such elements.

    Return type: int / np.integer / np.int32 / np.int64
    """
    if not 0 in X.diagonal():
        return X.diagonal().prod()
    print(X.diagonal().nonzero()[0])
    #print(X.diagonal().nonzero()[1])
    if len(X.diagonal().nonzero()) == 0:
        return -1
    return 1
    pass


x = np.load('public_tests/07_task1_vectorised_input/input_1/x.npy')
with open('public_tests/07_task1_vectorised_gt/output_1.pkl', 'rb') as f:
    res = pickle.load(f)

print(x)
print(res)
print(prod_non_zero_diag(x))


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    """
    Return True if both 1-d arrays create equal multisets, False if not.
    
    Return type: bool / np.bool_
    """
    pass


def max_after_zero(x: np.ndarray) -> int:
    """
    Find max element after zero in 1-d array, 
    return -1 if there is no such elements.

    Return type: int / np.integer / np.int32 / np.int64
    """
    pass


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """
    Sum up image channels with weights.

    Return type: np.ndarray
    """
    pass


def run_length_encoding(x: np.ndarray) -> (np.ndarray, np.ndarray):
    """
    Make run-length encoding.

    Return type: (np.ndarray, np.ndarray)
    """
    pass


def pairwise_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    Z = np.linalg.norm(X[:, None, :] - Y[None, :, :], ord=None, axis=-1)
    return Z
    pass
