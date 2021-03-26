# A dieter consumes calories[i] calories on the i-th day. Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):

#     If T < lower, they performed poorly on their diet and lose 1 point; 
#     If T > upper, they performed well on their diet and gain 1 point;
#     Otherwise, they performed normally and there is no change in points.

# Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for calories.length days.

# OK: O(N*k)

# Goal: O(N)
def diet_plan_performance(calories, k, lower, upper):
    points = 0
    for i in range(len(calories) - k + 1):
        sum_calories = sum(calories[i:i+k])
        if sum_calories<lower:
            points-=1
        elif sum_calories>upper:
            points+=1
    
    return points

calories = [1,2,3,4,5]
k = 1
lower = 3
upper = 3
expected = 0
print(diet_plan_performance(calories, k, lower, upper)) #0

calories = [3,2]
k = 2
lower = 0
upper = 1
print(diet_plan_performance(calories, k, lower, upper)) #1

calories = [11, 9, 6, 20, 4, 21, 20, 10, 28, 0]
k = 3
lower = 30
upper = 32
print(diet_plan_performance(calories, k, lower, upper)) #5