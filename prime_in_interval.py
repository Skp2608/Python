# program to check prime numbers in interval of a to b
n1=int(input("Enter value a :"))
n2=int(input("Enter value b :"))
for n in range (n1,n2+1):
    temp=0
    for i in range (2,n):
        if n%i==0:
            temp=0
            break
        else:
            temp=1
    if temp==1:
        print(f"{n}  ",end="")