#program 5 of DAY 6


import random

length = int(input('enter the size of random number list   :  '))

lst = []

for i in range(length):
    ran = random.randint(0,100)
    lst.append(ran)

print('\nThe array is  :  \n\n{}'.format(lst))    
    
    
fib_lst = [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368]

sum = 0
lst2 = []
for i in lst:
    if (i in fib_lst):
        sum = sum + i
        lst2.append(i)
print('\nThe fibonacci elements in the list are  :  {}'.format(lst2))
        
if sum in fib_lst:
    print('\nSum of fibonacci elements is  {}   which is a fibonacci number!!'.format(sum))
else:
    print('\nSum of fibonacci elements is  {}   which is not a fibonacci number!!'.format(sum))
