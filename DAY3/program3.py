#program 3 of DAY 3

string = input('Please enter the string\n')
print('The original string is : {} \n'.format(string))

duplicate_string = ''

for i in string:
    if i not in duplicate_string:
        duplicate_string = duplicate_string + i

print('the string after removing duplicate characters is : \n {}'.format(duplicate_string))
