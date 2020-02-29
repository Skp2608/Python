n=int(input("Enter a size of star :"))
for i in range (1,n+1):
    for j in range (1,n+1-i):
        print(" ",end="")
    for k in range (1,2*i):
        print("*",end="")
    print()
        