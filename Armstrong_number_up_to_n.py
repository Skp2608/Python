# Armstrong_number
import math
n1=int(input("Enter a number :"))
for n in range (1,n1+1):
    n=str(n)
    l=len(n)
    n=int(n)
    def power(n,l):
        s=0
        while n>0:
            r=n%10
            s+=pow(r,l)
            n=n//10
        return s
    a=power(n,l)
    if n==a:
        print(f"{n}  ",end="")
    