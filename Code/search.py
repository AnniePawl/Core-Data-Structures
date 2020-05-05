#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive beleft, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # Time: O(n) b/c iterating over each item
    # Space:

    for index, value in enumerate(array):
        # loop over all array values until item is found
        if item == value:
            return index  # found !
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # Time:
    # Space:
    if item is not None:
        if item == array[index]:
            return index
    else:
        return linear_search_recursive(array, item, index+1)


def linear_search_recursive1(array, item, index=0):
    if array[index] == item:  # base case
        return item  # found it!
    if index == len(list):
        return None  # did not find it
    else:
        return(linear_search_recursive1(array, item, index + 1))


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive beleft, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left = 0  # lowest item
    right = len(array) - 1  # highest item
    i = (left + right) // 2  # find middle
    while array[i] != item:
        if array[left] == item:
            return left
        elif array[right] == item:
            return right
        elif right - left == 1:
            return None
        if array[i] < item:
            left = i
        else:
            right = i
        i = (left + right) // 2
    return i

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if left is None and right is None:
        left = 0
        right = len(array) - 1

    if left > right:
        return None

    mid = (left + right) // 2
    if array[mid] == item:
        return mid  # item found

    elif array[mid] > item:
        right = mid - 1  # ignores the right (right)
        return binary_search_recursive(array, item, left, right)

    elif array[mid] < item:
        left = mid + 1  # ignores the left (left)
        return binary_search_recursive(array, item, left, right)
