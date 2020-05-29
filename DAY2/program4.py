number = int(input("Enter the value of N : "))

print("\n")

for i in range(number):
    print((number-i) * '*' + (i * 2) * ' ' + (number - i) * '*')
for i in range(number):
    print((i+1) * '*' + (number - i - 1) * ' ' + (number - i-1) * ' ' + (i+1) * '*')
