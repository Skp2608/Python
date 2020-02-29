n=int(input("Enter a size :"))
for i in range (1,n+1):
    for j in range (1,n+1):
        if i%2==0:
            print(f"# ",end="")
        else:
            print(f" #",end="")
    print()