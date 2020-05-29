#program 4 of DAY 5

def knapsack(weight, Lst):
    if weight == 0 or len(Lst) == 0:
        return 0
    if len(Lst) == 1:
        if Lst[0][0] > weight:
            return 0 
        return Lst[0][1]  
    if Lst[0][0] > weight:
        return knapsack(weight, Lst[1:])
    return max((Lst[0][1] + knapsack(weight - Lst[0][0], Lst[1:])), (knapsack(weight, Lst[1:])))


size =  int(input("Enter the number of items you want to enter  : "))

Lst = []

for i in range(size):
    print('\n')
    weight = int(input("Enter the weight of item  {}   :  ".format(i+1)))
    value  = int(input("Enter the value  of item  {}   :  ".format(i+1)))
    Lst.append((weight,value))

    

    
weight = int(input("\nEnter the size of Knapsack : "))
    
    
print("\nThe maximum value for the given weight value pair is ", knapsack(weight, Lst))
