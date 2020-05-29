n = int(input('enter the value of N : '))

print('\n')

for i in range(n):
    s = n-i
    print((str(s) + '*') * (s-1) + str(s))
    
for i in range(n):
    s=i+1
    print(str(s) + ('*' + str(s)) * (i))
