#!/usr/bin/env python3
n = int(input("Enter the number of matrix: "))

print('Enter matrix A: ')
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])  # an enter means the end of input

print('Enter matrix B: ')
b = []
for i in range(n):
    b.append([int(x) for x in input().split()]) # This is a list comprehension
                                                # input().split() is a list of string

c = [[0] * n for i in range(n)]    # an martix of n*n with all 0 element
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j] += a[i][k] * b[k][j]   # matrix multiply

print('The multiplication of matix A and B is: ')
print('-' * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end = ' ')
    print()
print('-' * 7 * n)
