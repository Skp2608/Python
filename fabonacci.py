n=int(input("Enter a size of fabonacci :"))
a=-1
b=1
for i in range (1,n+1):
    c=a+b
    print(f"{c}  ",end="")
    a=b
    b=c