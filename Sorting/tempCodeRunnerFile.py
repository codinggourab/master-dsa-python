def quickSort(arr, low = 0, high = None):
    if high is None:
        high = len(arr) - 1
        
    if low <  high:
        p_index = partition(arr, low, high)