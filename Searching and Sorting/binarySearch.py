"""
Implement Binary Search: given a sorted array and a target, return index of the target in the array or None is the target is not in the array.

    Compare the target to the middle element of the array.
    If target equals the middle element, return the index of the middle element.
    If the target is less than the middle element, then restrict to the lower half of the array
    If the target is greater than the middle element, restrict to the upper half.
    Repeat on the restricted portion.
    If restricted array becomes empty, fail.
"""
def binary_search(array, target):
    left = 0
    right = len(array)-1
    while left<=right:
        mid = (left+right)//2
        if target == array[mid]:
            return mid
        elif target<array[mid]:
            right = mid-1
        else:
            left = mid+1
    return None

a = [8, 13, 14, 26, 27, 28, 39, 50, 60, 61, 69, 73, 88, 93, 99]

print(binary_search(a, 8)) # 0

print(binary_search(a, 39)) # 6

print(binary_search(a, 99)) #14

print(binary_search(a, 10))  #None