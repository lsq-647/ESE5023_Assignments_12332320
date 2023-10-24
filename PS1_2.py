# 2. Matrix multiplication
import random
import numpy as np
M1 = np.random.randint(0,50,(5,10))
M2 = np.random.randint(0,50,(10,5))
print(M1)
print(M2)

def Matrix_multip():
    rows1 = 5
    columns1 = 10
    rows2 = 10
    columns2 = 5
    
    result = []
    for i in range(rows1):
        row = []
        for j in range(columns2):
            sum = 0
            for k in range(columns1):
                sum += M1[i, k] * M2[k, j]
            row.append(sum)
        result.append(row)
    return result
Matrix_multip()
