# Compute the correlation of two lists

import numpy as np

def cor(arr1: list[float], arr2: list[float]) -> float:
    if len(arr1) != len(arr2):
        raise ValueError("The length of the two lists does not match")
    
    # Compute the variance
    def var(arr: list[float]) -> float:
        mean_ = np.mean(arr)
        mean_ = np.mean(arr)
        mean_diff_squared = [(num-mean_)**2 for num in arr]
        return np.mean(mean_diff_squared)
    # Compute covariance
    def cov(arr1: list[float], arr2: list[float]) -> float:
        arr_product = [x * y for x, y in zip(arr1, arr2)]
        mean_arr1 = np.mean(arr1)
        mean_arr2 = np.mean(arr2)
        arr_product = [x * y for x, y in zip(arr1, arr2)]
        return np.mean(arr_product) - mean_arr1 * mean_arr2
    # Compute correlation
    return cov(arr1, arr2)/((var(arr1)*var(arr2))**0.5)


        
        
        
    