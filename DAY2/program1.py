number = int(input("Enter a number : \n"))

#number is odd/even??
print('\n\n')
if(number % 2 == 0):
    print(number ,"is an Even Number \n")
else:
    print(number ,"is an Odd Number \n")

#is number prime??
temp = number
a = 2
k = temp // 2
while k >= a:
    if temp % a == 0:
        print(number ,"is not a Prime Number \n")
        break
    a += 1
    k = temp // a
if(k<a):
    print(number ,"is a Prime Number \n")
    
#is number palindrome??
ns = str(number)
l = len(ns)
for i in range(l // 2):
    if ns[i] == ns[l - 1 - i]:
        continue
    else:
        print(number, "is not a Palindrome Number \n")
        break
else:
    print(number, "is a Palindrome Number \n")
    
#is number armstrong??
sum = 0  
temp = number  
while temp > 0:  
    digit = temp % 10
    sum += digit ** 3  
    temp //= 10  
if number == sum:  
    print(number ,"is an Armstrong Number \n")
else:
    print(number ,"is not an Armstrong Number \n")
