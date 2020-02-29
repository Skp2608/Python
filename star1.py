n = int(input("Enter a size of star :"))
for i in range(1, n+1):
    for j in range(1, 5+i):
        if j <= (n-i):
            print(" ", end="")
        else:
            print("*", end="")
    print()
