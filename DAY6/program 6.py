#program 6 of DAY 6

import random

a = [8,9,11,12,15,21,2,3,4,6,7]
b = [8,9,11,12,16,13,1,5,6,21]
c = [1,2,3,4,5,6,7,8,9]

given_list = a

smallest_value = min(given_list)
index_of_smallest_value = given_list.index( smallest_value )

list_before_smallest_no = given_list[0:index_of_smallest_value]

list_after_smallest_no  = given_list[index_of_smallest_value+1:]



a = list_before_smallest_no == sorted(list_before_smallest_no) #To check sorting 
b = list_after_smallest_no  == sorted(list_after_smallest_no) #To check sorting

c = given_list[0] > given_list[-1] #To check rotation



if a==b==c==True:
    print('___YES , The given list is sorted and rotated____')
else:
    print('Sorry , The given array is not sorted and not rotated')
