#Recursion lecture from the week of March 29th
#Knapsack problem, get the highest value
def kp(cap,ws,vs,i,val):
    #base case
    if i>=len(ws):
        return val
    #if the weight of an item exceeds the capacity of the knapsack
    #if it doesn't fit, leave it and check the next item
    if ws[i] > cap:
        return kp(cap,ws,vs,i+1,val)
    #if it does fit, find the total value for if we take the item, then find the total value if we leave it
    #take item
    val_take = kp(cap-ws[i],ws,vs,i+1,val+vs[i])
    #leave item
    val_leave = kp(cap,ws,vs,i+1,val)
    #return the max of val_take and val_leave to determine max total value
    return max(val_take,val_leave)


cap = 40
weights = [10,40,20]
values = [100,120,80]
print(kp(cap,weights,values,0,0)) #180

cap = 50
weights = [10,20,30]
values = [60,100,120]
print(kp(cap,weights,values,0,0)) #220