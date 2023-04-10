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
    
    p1 = multiply(a11, subtract(b12, b22))
    p2 = multiply(add(a11, a12), b22)
    p3 = multiply(add(a21, a22), b11)
    p4 = multiply(a22, subtract(b21, b11))
    p5 = multiply(add(a11, a22), add(b11, b22))
    p6 = multiply(subtract(a12, a22), add(b21, b22))
    p7 = multiply(subtract(a11, a21), add(b11, b12))
    
    c11 = add(subtract(add(p5, p4), p2), p6)
    c12 = add(p1, p2)
    c21 = add(p3, p4)
    c22 = subtract(subtract(add(p5, p1), p3), p7)
    
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

def subtract(a, b):
    n = len(a)
    c = []
    for i in range(n):
        c.append([a[i][j] - b[i][j] for j in range(len(a[i]))])
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