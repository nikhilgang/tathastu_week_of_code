#program 13 of DAY 6

my_lst = []
new_lst = []
size = int(input('Enter the number of elements you want to enter in the list   :   '))

for i in range(size):
    my_lst.append(input('Enter the value of element  {}  :  '.format(i+1)))
    
for i in my_lst:
    new_lst.append(float(i))


flag = 0
print('\n')
for i in range(size-2):
    for j in range(i+1,size-1):
        for k in range(i+2,size):
            
            sum = new_lst[i] + new_lst[j] + new_lst[k]
            
            if 1 < sum < 2:
                
                flag+=1
            
                print('The triplet  is  {} , {} , {} having sum  =  {}\n'.format(new_lst[i] , new_lst[j] , new_lst[k] , sum))
            
if flag == 0:
    print('No such triplet is found for the given list')
