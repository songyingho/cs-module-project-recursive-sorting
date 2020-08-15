# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # check base case
    if end >= start:
        mid = (start + end) // 2

        # if element is present in middle itself
        if arr[mid] == target:
            return mid
        # if element is smaller than mid, then it must be in left subarray
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid-1)
        # if element is larger than mid, then it must be in right subarray
        else:
            return binary_search(arr, target, mid+1, end)
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
