
import numpy as np


def quicksort(arr):
    if arr is None or len(arr) < 2:
        return arr
    
    pivot = arr[-1] # last item in array
