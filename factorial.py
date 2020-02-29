#program to find factorial of a number
def fun(n):
    f=1
    for i in range (1,n+1):
        f*=i
    return f
n=int(input("Enter a number :"))

print(f"Factorial up to n term is {fun(n)}")