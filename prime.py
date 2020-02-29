# program to check prime numbers
n=int(input("Enter a number :"))
temp=0
for i in range (2,n):
    if n%i==0:
        temp=0
        print(f"Given number is not prime")
        break
    else:
        temp=1
if temp==1:
    print(f"Given number is prime")

