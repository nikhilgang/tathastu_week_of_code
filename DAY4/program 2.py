#program 2 of DAY 4

sL = int(input("Enter number of tuples in list: "))
sT = int(input("Enter number of elements in each tuple: "))

ls = []

for i in range(sL):
    print("Enter elements of Tuple", i + 1)
    tup = []
    for j in range(sT):
        tup.append(int(input("Enter element " + str(j + 1) + ": ")))
    ls.append(tuple(tup))

n = int(input("Enter the Nth index to sort the list: "))

ls.sort(key = lambda x : x[n])  #Sorts the nth element of each tuple in ascending order

print("\nSorted tuple list by Nth tuple:",ls)
