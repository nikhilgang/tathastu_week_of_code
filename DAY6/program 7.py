#program 7 of DAY 6

def ackerman(m,n):
    if m==0:
        return n+1
    if n==0:
        return ackerman(m-1,1)
    
    n2 = ackerman(m,n-1)
    return ackerman(m-1,n2)


a,b = int(input("Enter first value:")),int(input("Enter second value:"))
print("\nThe computed ackerman value is:", ackerman(a,b))
