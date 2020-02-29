# Armstrong_number
import math
n=input("Enter a number :")
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
    print("Yes")
else:
    print("No")


        
