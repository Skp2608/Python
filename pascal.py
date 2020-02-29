n=int(input("Enter a size of pascal :"))
for i in range (1,n+1):
    for j in range (1,i+1):
        if j==1 or j==i:
            print("1 ",end="")
        else:
            r=i-1

            print("  ",end="")
    print()