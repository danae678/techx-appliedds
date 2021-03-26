# Find the first non-repeated character in a string.

# Some things you can reason from the example:

# The return value is the non-repeated character itself, as opposed to the index or some other value

# Example:

#   Input:  input_string = "supercalifragilisticexpialidocious"

#   Output: "f"

import collections
def first_nonrepeat(word):
    dictionary = collections.Counter(word)
    for i in dictionary:
        if dictionary[i] == 1:
            return i
    return None
    
print(first_nonrepeat("hello"))
print(first_nonrepeat("supercalifragilisticexpialidocious"))