#program 2 of DAY 5

size = int(input('Enter the number of total values  :  '))


lst = []
for i in range(size):
    lst.append(int(input('Please enter the value  :  ')))
    
    

def rep(lst):
    
    for i in range(size-1):
        lst[i] = max(lst[i+1:])
    return lst

    
print('The list obtained after replacing all values with maximun value in its right side  :  {}'.format(rep(lst)))
    
