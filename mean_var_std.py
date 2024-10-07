import numpy as np

def calculate(arr):
    if len(arr) != 9:  
        raise ValueError("List must contain nine numbers.")
    else:
     array = np.array(arr).reshape(3, 3)

    # Calculate means
     mean_row = np.mean(array, axis=0)
     mean_col = np.mean(array, axis=1)
     mean_raw = np.mean(array)

    # Calculate variances
     var_row = np.var(array, axis=0)
     var_col = np.var(array, axis=1)
     var_raw = np.var(array)

    # Calculate standard deviations
     std_row = np.std(array, axis=0)
     std_col = np.std(array, axis=1)
     std_raw = np.std(array)

    # Calculate mins
     min_row = np.min(array, axis=0)
     min_col = np.min(array, axis=1)
     min_raw = np.min(array)

    # Calculate maxs
     max_row = np.max(array, axis=0)
     max_col = np.max(array, axis=1)
     max_raw = np.max(array)

    # Calculate sums
     sum_row = np.sum(array, axis=0)
     sum_col = np.sum(array, axis=1)
     sum_raw = np.sum(array)

    # Create a dictionary to hold the results
     calculations = {
        'mean': [mean_row.tolist(),mean_col.tolist(),mean_raw],
        'variance': [var_row.tolist(),var_col.tolist(),var_raw],
        'standard deviation': [std_row.tolist(),std_col.tolist(),std_raw],
        'max': [max_row.tolist(),max_col.tolist(),max_raw],
        'min': [min_row.tolist(),min_col.tolist(),min_raw],
        'sum': [sum_row.tolist(),sum_col.tolist(),sum_raw]
     }

    return calculations

