import numpy as np
import time

def multiply(a, b):
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]
    
    a11 = [row[:n//2] for row in a[:n//2]]
    a12 = [row[n//2:] for row in a[:n//2]]
    a21 = [row[:n//2] for row in a[n//2:]]
    a22 = [row[n//2:] for row in a[n//2:]]

    b11 = [row[:n//2] for row in b[:n//2]]
    b12 = [row[n//2:] for row in b[:n//2]]
    b21 = [row[:n//2] for row in b[n//2:]]
    b22 = [row[n//2:] for row in b[n//2:]]

    c11 = add(multiply(a11, b11), multiply(a12, b21))
    c12 = add(multiply(a11, b12), multiply(a12, b22))
    c21 = add(multiply(a21, b11), multiply(a22, b21))
    c22 = add(multiply(a21, b12), multiply(a22, b22))

    result = []
    for i in range(n):
        if i < n//2:
            result.append(c11[i] + c12[i])
        else:
            result.append(c21[i-n//2] + c22[i-n//2])
    return result

def add(a, b):
    n = len(a)
    c = []
    for i in range(n):
        c.append([a[i][j] + b[i][j] for j in range(n)])
    return c

manual = input("Use custom matrices? (y/n) ")
if (manual == "y"):
    n = int(input("Enter dimension that is a power of 2: "))
    print("Enter matrix 1 entries (left to right, separated by space): ")
    entries = list(map(int, input().split()))
    matrixA = np.array(entries).reshape(n, n)
    print("Enter matrix 2 entries (left to right, separated by space): ")
    entries = list(map(int, input().split()))
    matrixB = np.array(entries).reshape(n, n)

else:
    n = int(input("Enter dimension that is a power of 2: "))
    matrixA = np.random.randint(10, size=(n, n))
    matrixB = np.random.randint(10, size=(n, n))

start = time.time()
newMatrix = multiply(matrixA, matrixB)

for i in newMatrix:
    print(i)

end = time.time()
print("\nExecuted in ", (end-start) * 10**3, "ms")