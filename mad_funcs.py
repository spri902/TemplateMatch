import numpy as np 

def mad_func_li(arr):
    """ Median Absolute Deviation: Using the formulation in Li and Zhan 2018
    Pushing the limit of earthquake detection with DAS and template matching
    """
    # arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    mean = np.mean(arr)
    med = np.median(arr)
    return np.median(np.abs(mean - med))

def mad_func_shelly(arr):
    """ Median Absolute Deviation: Using the formulation in Li and Zhan 2018
    Pushing the limit of earthquake detection with DAS and template matching
    """
    # arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    # mean = np.mean(arr)
    med = np.median(arr)
    return np.median(np.abs(arr - med))

def detections(cc_arr, mode='shelly'):
    """ using detection significance from Li and Zhan 2018
    det = (peak - med) / mad
    """
    
    med = np.median(cc_arr)
    if mode == 'shelly':
        mad = mad_func_shelly(cc_arr)
    elif mode == 'li':
        mad = mad_func_li(cc_arr)

    det = (cc_arr - med) / mad
    return det,mad
