from __future__ import print_function
from __future__ import division

# Shell Sort involves sorting elements which are away from each other. It is
# essentially a variation of insertion sort. In insertion sort,
# we move elements only one position ahead. So, if the largest number resides
# on beginning of the list, it has to be moved all the way to the end one by
# one. Shell sort defines a 'gap' parameter (or a width parameter). Each time,
# an element at index i and index i + gap is compared and seapped if necessary
# and hence, elements are swapped faster(instead of one by one in case of
# insertion sort). After each pass we reduce this gap by 2 and continue the
# process. Insertion sort is special case of shell sort when gap is 1.

# Time complexity: O(n^2) (worst-case)
# references: https://www.youtube.com/watch?v=ddeLSDsYVp8
#             https://www.youtube.com/watch?v=SHcPqUe2GZM


def shell_sort(_list):
    # initially define gap as half the list length
    gap = len(_list) // 2

    while gap > 0:
        # we iterate the list from gap to end of array and compare elements to
        # its left
        for i in range(gap, len(_list)):
            temp = _list[i]
            idx = i
            # compare temp across the left sublist until its in the right
            # postion
            while idx >= gap and temp < _list[idx - gap]:
                _list[idx] = _list[idx - gap]
                idx = idx - gap

            _list[idx] = temp

        gap = gap // 2
    return _list


# assert shell_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
# assert shell_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
# assert shell_sort([9, 6, 7, 4, 5]) == [4, 5, 6, 7, 9]
