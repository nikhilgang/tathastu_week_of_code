no_of_user = int(input('enter the number of users\n'))
for i in range(no_of_user):
    print('enter the details of user {} \n'.format(i+1))
    name=input('please enter the name of user {} \n'.format(i+1))
    age=int(input('please enter the age of user {} \n'.format(i+1)))
    gender=input('please enter the gender of user {} \n'.format(i+1))
    
    
    print('\nThe name of user {} is {} and age is {} and gender is {}'.format(i+1,name,age,gender))
