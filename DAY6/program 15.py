#program 15 of DAY 6

n = int(input("Enter size of array  :   "))
arr = []

for i in range(n):
    arr.append(int(input("Enter value  :  ")))

count = 0
print('\nThe array is  :  {}\n'.format(arr))
for i in range(1, n-1):
    flag = 0
    for j in range(i):
        if arr[j] > arr[i]:
            flag = 1
            break
    for j in range(i+1, n):
        if arr[j] < arr[i]:
            flag = 1
            break

    if flag==0:
        print("{}  is the answer at location  {}  in the array.".format(arr[i],i+1))
        count = 0
        break
        
    else:
        count+=1

        
if count != 0:        
    print("\nNo such number found.")
