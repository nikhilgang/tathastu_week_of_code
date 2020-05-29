#program 5 of DAY 3

lst1 = list()
lst2 = list()

size_lst1 = int(input('enter the size of list 1 \n'))
print('enter the elements of list 1 one by one \n')

for i in range(size_lst1):
    a = input('enter the data {}    '.format(i+1))
    lst1.append(a)

    
size_lst2 = int(input('enter the size of list 2 \n'))    
print('enter the elements of list 2 one by one \n')
        
for i in range(size_lst2):
    a = input('enter the data {}    '.format(i+1))
    lst2.append(a)
    
    
set1 = set(lst1)
set2 = set(lst2)

print('\n')

print('the list 1 is : \n {}'.format(lst1))
print('the list 2 is : \n {}'.format(lst2))

updated_list = list(set1.intersection(set2))
print('\nthe updated list after intersection operation is : \n {} '.format(updated_list))
