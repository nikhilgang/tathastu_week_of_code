#program 11 of DAY 6

import random
length = int(input('enter the size of list  :  '))

lst = []
for i in range(length):
    lst.append(random.randint(0,10))

print('\nThe list of elements is  {}'.format(lst))

lst2 = sorted(lst)

sum = lst2[-1] * lst2[-2] * lst2[-3]

print(sum)
