#program 5 of DAY 5


lst = [5,2,55,11,56,23,10,19,4,7,9,28,16]
odd = []
even =[]
for i in lst:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
odd.sort()
even.sort()
lst = odd[::-1] + even
print('The array having odd no sorted in descending order and even no in ascending order is  :  \n\n{}'.format(lst))
