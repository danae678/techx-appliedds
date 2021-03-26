# Given a list of numbers return the number that occurs the majority of the time. If no number occurs more than 50% of the time, return None.
#   [2, 7, 9, 2, 2, 3, 2] => 2
#   [] => None
#   [1, 2] => None
import collections

def majority_element(numbers):
  dictionary = collections.Counter(numbers)
  for i in dictionary:
    if dictionary[i] >= len(numbers)/2:
      return max(dictionary, key=dictionary.get)
    else:
      return None
print(majority_element([1,2]))