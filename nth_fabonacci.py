# Python Program for n-th Fibonacci number?
def fabonacci(n):
    if n<0:
        return f"Incorrect Input"
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fabonacci(n-1)+fabonacci(n-2)

n=int(input("Enter a number for n-th Fibonacci number :"))
print(fabonacci(n))