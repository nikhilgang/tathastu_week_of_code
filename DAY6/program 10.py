#program 10 of DAY 6

length = int(input('Enter the number of sorted lists  :  \n'))

main_lst = []

for i in range(length):
        i = []
        main_lst.append(i)
    
for i in range(len(main_lst)):
    size = int(input('\n\nenter the size of list {}    :    '.format(i+1)))
    for j in range(size):
        main_lst[i].append(int(input('enter the value   {}   for list   {}     :  '.format(j+1,i+1))))
        
    main_lst[i] = sorted(main_lst[i])
    
print('\nThe merged sorted lists are    :    {}'.format(main_lst))

main = []

for i in range(length):

    for j in range(len(main_lst[i])):
          main.append(main_lst[i][j])

        
print('The sorted list is             :    {}'.format(sorted(main)))
