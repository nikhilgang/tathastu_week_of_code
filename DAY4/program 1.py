#program 1 of DAY 4


n = int(input('enter the number of elements in the tuple    :   '))
print('\n')
tup = []
for i in range(n):
    element = input('enter the element {} \n'.format(i+1))
    
    tup.append(element)
    
tup = tuple(tup)

print('\nthe tuple is \n {}'.format(tup))

num = input('enter the element whose occurrence is to be counted   :   ')

print('the occurence of element   {}   is    {} times'.format(num,tup.count(num)))

