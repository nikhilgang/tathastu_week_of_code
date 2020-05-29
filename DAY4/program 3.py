#program 3 of DAY 4

size = int(input('enter the size of dictionary'))

my_dict = {}

for i in range(size):
    
    key = input('\nenter the key     :    ')
    my_dict[key] = int(input('enter the value   :    '))


print('\nthe 2nd largest value is   :   {}'.format(list(sorted(my_dict.values()))[-2]))
