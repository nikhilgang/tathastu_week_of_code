#program 1 of DAY 6

def minDeletions(X, n):

    Y = X[::-1]

    lookup = [[0 for x in range(n + 1)] for y in range((n + 1))]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1

            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])

    return n - lookup[n][n]

st = str(input("Enter a string: "))
n = len(st)
print("The minimum number of deletions required are", minDeletions(st, n))
