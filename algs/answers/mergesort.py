import numpy as np


def merge(a, b):
    i = 0 # a idx
    j = 0 # b idx
    k = 0 # merged idx
    merged = [0] * (len(a) + len(b))
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged[k] = a[i]
            i += 1
        else:
            merged[k] = b[j]
            j += 1
        k += 1
    
    while i < len(a):
        merged[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        merged[k] = b[j]
        j += 1
        k += 1
    
    return merged


def merge_sort(arr):
    if arr is None or len(arr) < 2:
        return arr
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    return merge(left, right)

if __name__ == '__main__':
    for i in range(1000):
        test = np.random.randn(i)
        answer = sorted(test)
        if merge_sort(test) != answer:
            print(merge_sort(test))
            print(answer)
            print()
