# Given a number, find the sum of its digits using recursion.

# Examples:

# Input : 12345
# Output : 15

# Input : 45632
# Output :20

def sumOfDigits(num):
    negative = 1
    if num == 0:
        return 0
    if num<0:
        num = num*-1
        negative = -1
        
    return ((num%10 + sumOfDigits(num//10))*negative)