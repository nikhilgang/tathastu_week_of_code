number = int(input("Enter the value of N : "))

print("\n")

for i in range(number):
    print(" " * i + "*" + "  " * (number - 1 - i) + "*")

for i in range(number):
    print(" " * (number - 1 - i) + "*" + "  " * i + "*")
