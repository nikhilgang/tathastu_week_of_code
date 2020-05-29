#program 1 of DAY 5

def rep(number):
    return(int(number.replace('5','0',-1)))

no = input('Enter the number   :  ')
print("The number obtained after replacing all 5's with 0's is   :  {}".format(rep(no)))
