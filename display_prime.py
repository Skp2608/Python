#  program to display prime numbers
n=int(input("Enter a number :"))
print("Prime Number is \n2 ",end="")
for i in range (n+1):
    temp=0
    for j in range (2,i):
        if i%j==0:
            temp=0
            break
        else:
            temp=1
    if temp==1:
        print(f"{i} ",end="")
        