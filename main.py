"""
Numeric Matrix Processor
author: Arturexp
"""
matrix1 = []
matrix2 = []
result = []

a, b = map(int, input().split())
for i in range(a):
    matrix1.append(list(map(int, input().split())))

c, d = map(int, input().split())
for i in range(c):
    matrix2.append(list(map(int, input().split())))

if a == c and b == d:
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(b)] for i in range(a)]
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in result]))
else:
    print("ERROR")
