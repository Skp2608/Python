# -*- coding: utf-8 -*-
"""
Matrix Multiplication

@author: SK
"""
i1=int(input("Number of ROWS of 1st matrix:"))
j1=int(input("Number of COLUMNS of 1st matrix:"))
i2=int(input("Number of ROWS of 2nd matrix:"))
j2=int(input("Number of COLUMNS of 2nd matrix:"))
a=[]
b=[]
c=[]

if(j1==i2):
    print("\nEnter elements of 1st Matrix:\n")
    for i in range(i1):
        l=[int(j) for j in input().split()]
        a.append(l)

    print("\nEnter elements of 2nd Matrix:\n")
    for i in range(i2):
        l=[int(j) for j in input().split()]
        b.append(l)
    
    for i in range(i1):
        l=[]
        for j in range(j2):
            l.append(0)
        c.append(l)
            
    for i in range(len(a)):
        for j in range(len(b[0])):
            sum=0
            for k in range(len(b)):
                sum+= a[i][k] * b[k][j]
                c[i][j]=sum

    print("\nMatrix Obtained after Multiplication is:\n")
    for i in range(i1):
        for j in range(j2):
            print(c[i][j],end=" ")
        print("",end="\n")
    
else:
    print("\nMatrix multiplication not possible!\nBecause No. of COLUMNS of 1st matrix is not equal to No. of ROWS of 2nd Matrix.")
