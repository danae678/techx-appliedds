# Find a number that appears an odd number of times in an array. You have an array that contains integers. Each number appears an even number of times, except one number will appear an odd number of times. Find the number that appears an odd number of times.

# Example:
# Input: numbers = [1, 4, 4, 1, 6, 4, 4]
# Output: 6
import collections
def odd_occurences(nums):
    dictionary = collections.Counter(nums)
    for i in dictionary:
        if dictionary[i] % 2 ==1:
            return i
    return None

numbers = [1, 4, 4, 1, 6, 4, 4]
print(odd_occurences(numbers))