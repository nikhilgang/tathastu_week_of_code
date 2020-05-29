#program 2 of DAY 6

import random

length = int(input('enter the length of array  :  '))

lst = []

for i in range(length):
    lst.append(random.randint(0,1))
print('\nThe array containing 0 and 1 is  :   {}'.format(lst))

a=0
b=0

for i in lst:
    if i ==0:
        a+=1
    elif i==1:
        b+=1

    
    
lst2 = []
for i in range(a):
    lst2.append(0)
for i in range(b):
    lst2.append(1)
    
print('\nThe sorted array is  :  {}'.format(lst2))
