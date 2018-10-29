from __future__ import print_function
from __future__ import division

# BrickSort (also called odd-even sort) is a variation of bubble-sort.
# This algorithm is divided into two stages - odd and even.
# In odd phase, you take elements in odd indexes and compare it to the next
# element(and swap them if necessary). In even phase you repeat the same
# process but with even indices. Both stages are repeated till array is sorted.

# Time complexity: O(n^2)
# Space complexity : O(1) (Inplace sorting algorithm)
# references: https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort


def brick_sort(arr):
    # Initially array is unsorted
    _sorted = False
    while _sorted is False:
        _sorted = True
        # odd stage
        for i in range(1, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                _sorted = False
        # even stage
        for i in range(0, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                _sorted = False

    return arr


# assert brick_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
# assert brick_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
# assert brick_sort([9, 6, 7, 4, 5]) == [4, 5, 6, 7, 9]
