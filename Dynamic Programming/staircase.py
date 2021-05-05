"""
You can walk up stairs 1 or 2 steps at a time. 

Each step has a positive integer cost to step on.

Find the minimum cost to reach the top step, assuming that you start on the base, before any of the steps.

Input: costs = [3,2,4,3,1]
Output: 5
Explanation: From the base we can step on index 0 (cost 3) or index 1 (cost 2). We go to step 1, 
and from there to step 3.  From there we can go up 2 steps to the top.

Input: costs = [5, 4, 2, 6, 3, 1, 5]
Output: 4 + 2 + 3 + 1 = 10
Explanation: base -> 1, 1 -> 2, 2 -> 4, 4 -> 5, 5 -> top

Input: costs = [1, 2, 10, 2]
Output: 2 + 2 = 4
Explanation: base -> 1, 1 -> 3, 3 -> top
"""
#recursive solution
def min_step_cost_aux(lst,n):
    if n<2:
        return 0
    return min(
        lst[n-1] + min_step_cost_aux(lst,n-1),lst[n-2] + min_step_cost_aux(lst,n-2))

def min_step_cost(lst):
    return min_step_cost_aux(lst, len(lst))
    
#memoization
def min_step_cost_aux(lst,n,cache):
    if n in cache:
        return cache[n]
    cache[n] = min(
        lst[n-1] + min_step_cost_aux(lst,n-1,cache),lst[n-2] + min_step_cost_aux(lst,n-2,cache))
    return cache[n]
def min_step_cost(lst):
    cache = {0:0, 1:0}
    return min_step_cost_aux(lst, len(lst), cache)

#dynamic programming solution
def min_step_cost(lst):
    cache = {0:0, 1:0}
    n = len(lst)
    for i in range(2,n+1):
        cache[i] = min((lst[i-1]+cache[i-1]),(lst[i-2]+cache[i-2]))
    
    return cache[n]
    