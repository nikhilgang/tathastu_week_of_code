#program 14 of DAY 6


def rot90CW(mat): 
    N = len(mat[0]) 
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            temp = mat[i][j] 
            mat[i][j] = mat[N - 1 - j][i] 
            mat[N - 1 - j][i] = mat[N - 1 - i][N - 1 - j] 
            mat[N - 1 - i][N - 1 - j] = mat[j][N - 1 - i] 
            mat[j][N - 1 - i] = temp 


n = int(input("Enter size of square matrix   :   "))

mat = []

for i in range(n):
    a =[] 
    for j in range(n):
         a.append(int(input("Enter value  :  "))) 
    mat.append(a)

print('\nThe original matrix array is  : \n')
for i in range(N): 
    print(mat[i])   

    
rot90CW(mat) 
N = len(mat[0]) 

print('\n\nThe rotated matrix is  :  \n')
for i in range(N): 
    print(mat[i])
