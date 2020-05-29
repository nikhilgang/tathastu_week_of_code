#program 6 of DAY 4 - BONUS CODE


d = []
array = []
result = []


dict_size = int(input('enter the total words in the dictionary  :  '))

for i in range(dict_size):
    d.append(input('enter the word {}  :  '.format(i+1)))

    
    
arr_size = int(input('enter the total characters available  :  '))

for i in range(arr_size):
    array.append(input('enter the character {}  :  '.format(i+1)))
    

for value in d: 
    if set(value).issubset(set(array)):
        result.append(value)
        
print('\n')
print('the words formed by given character array are  :  {}'.format(result))
