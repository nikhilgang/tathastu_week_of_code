#program 3 of DAY 6

import random

length = int(input('enter the size of random number list    :   '))

lst = []
for i in range(length):
    ran = random.randint(-10,10)
    lst.append(ran)
print('the random number list is :  \n\n{}'.format(lst))


lst2 = []

for i in lst:
    if i >= 0:
        lst2.append(i)

if 0 not in lst2:
    lst2.append(0)
lst2.sort()


small = min(lst2)
for i in lst2:
    if ((small + 1) not in lst2):
        print('\nthe smallest positive number is  :  {}'.format(small+1))
        break
    else:
        small = small + 1
