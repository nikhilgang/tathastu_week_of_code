#program 9 of DAY 6


import random
length = int(input('enter the size of list  :  '))

lst = []
for i in range(length):
    lst.append(random.randint(-100,100))

print('\nThe list of elements is  {}'.format(lst))


lst = sorted(lst)    

element = int(input('\nenter the value of k    :  '))


short = lst[element-1]
print(lst)
print('\nThe {} smallest element in the list is  {} .'.format(element,short))
