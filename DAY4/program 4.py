#program 4 of DAY 4

size = int(input('enter the size of dictionary'))

my_dict = {}

for i in range(size):
    
    key = input('\nenter the key     :    ')
    my_dict[key] = int(input('enter the value   :    '))
    
result_dict = {}    
    
for key , value in my_dict.items():
    if value not in result_dict.values():
        result_dict[key] = value
        
print('the dictionary after removing duplicate values is  :  {}'.format(result_dict))
