# Program to add two numbers in Python
def sum_ab(a, b):
    return (a+b)


a, b = input("Enter 2 number :").split()
a = int(a)
b = int(b)
print(f"Sum of 2 number is {sum_ab(a,b)}")
