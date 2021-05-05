"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Examples:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
"""

def generateParenthesis(n):
    return helper(n,"",0,0)
    
def helper (n, currentStr, opens_used, closed_used):
    if opens_used == n and closed_used ==n:
        return [currentStr]
    results = []
    if opens_used > closed_used:
        #append closed
        results += helper(n, currentStr + ")", opens_used, closed_used+1)
    if opens_used < n:
        #append open
        results += helper(n, currentStr + "(", opens_used+1, closed_used)
        
    return results

print(generateParenthesis(4))