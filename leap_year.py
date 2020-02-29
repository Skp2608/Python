# program to check leap year
y=int(input("Enter a year :"))
if y%4==0 and y%100!=0:
    print("Given year is leap year")
elif y%400==0:
    print("Given year is leap year")
else:
    print("Given year is not leap year")
