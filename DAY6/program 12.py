#program 12 of DAY 6

size = int(input("Enter number of strings: "))
lst = []

for i in range(size):
     lst.append(str(input("Enter string {}  :  ".format(i+1))))
    
lst.sort()
print('\nThe list of strings is  :  {}  \n'.format(lst))
n1 = len(lst[0]) 
n2 = len(lst[size-1]) 

result = "" 
      
j = 0
i = 0
while(i <= n1 - 1 and j <= n2 - 1): 
    if (lst[0][i] != lst[size-1][j]): 
        break
    result += (lst[0][i]) 
    i += 1
    j += 1

print("Longest common prefix:", result)
