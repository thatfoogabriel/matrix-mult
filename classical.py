import numpy as np
import time

manual = input("Use custom matrices? (y/n) ")
if (manual == "y"):
    n = int(input("Enter dimension: "))
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

newMatrix = np.random.randint(1, size=(n, n))
start = time.time()
for i in range(n):
    for j in range(n):
        for k in range(n):
            newMatrix[i][j] += matrixA[i][k] * matrixB[k][j]

for i in newMatrix:
    print(i)

end = time.time()
print("\nExecuted in ", (end-start) * 10**3, "ms")