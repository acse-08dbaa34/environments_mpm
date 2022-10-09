import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc

import pandas as pd

__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'data_frame']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def data_frame(list1, list2):
    s1 = pd.Series(list1)
    s2 = pd.Series(list2)
    data_dict = {"name":s1, "number":s2}
    return pd.DataFrame(data_dict)