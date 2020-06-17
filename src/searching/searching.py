# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    """
    recursive binary search
    """
    # cases where we should return empty arrays
    if len(arr) == 0: # or start >= end(?)
        return -1
    # setting mid point 
    mid = (start + end) // 2
    # return index if found
    if target == arr[mid]:
        return mid
    # recurse!
    elif target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
# Your code here

