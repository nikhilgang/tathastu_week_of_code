#program 4 of DAY 3

lst=list()
while(True):
    a=input('enter the list value\n')
    lst.append(a)
    a = input('do you want to enter more values : tap "y/Y" or "n/N"     :    ')
    
    if(a=='y' or a=='Y'):
        pass
    elif(a=='n' or a=='N'):
        break
        
print('\n\n')
print('the list created is : \n {}'.format(lst))

dup_lst = list()

for i in lst:
    if i not in dup_lst:
        dup_lst.append(i)
print('\n')
print('the list after removing duplicate values is : \n {}'.format(dup_lst))
