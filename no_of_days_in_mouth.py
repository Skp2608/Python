# C++ program to find total number of days in given month of year

m=int(input("Enter a mouth like 1,2 ...:"))
if m==2:
    y=int(input("Please enter a year :"))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    d=31
elif m==4 or m==6 or m==9 or m==11:
    d=30
elif m==2:
    if (y!=100 and y%4==0) or y%400==0:
        d=29
    else:
        d=28
print(f"Number of days in mouth :{d}")
