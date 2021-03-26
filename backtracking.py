#Recursion lecture

def ssp(nums, target,i):
    if i>=len(nums):
        return target==0
    if ssp(nums,target-nums[i],i+1):
        return True
    return ssp(nums,target,i+1)

print(ssp([3,1,5],8,0))