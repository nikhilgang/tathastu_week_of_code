number = int(input("enter the number you want to print in fibonacci series : "))
if number > 1:
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,number,1):
        c=a + b
        a = b
        b = c
        print(c)
else:
    print('0')
