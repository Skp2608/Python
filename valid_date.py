# C++ program to check given date is in valid format or not
y,m,d=input("Enter year : Month : Day  ").split(":")
y=int(y)
m=int(m)
d=int(d)

def valid(y,m,d):
    if y>0 and 0<m<=12 and 0<d<=31:
        return f"Given date is valid "
    return f"Given date is not valid "

def valid_30(y,m,d):
    if y>0 and 0<m<=12 and 0<d<31:
        return f"Given date is valid "
    return f"Given date is not valid "

def valid_28(y,m,d):
    if (y!=100 and y%4==0) or y%400==0:
        if y>0 and 0<m<=12 and 0<d<=29:
            return f"Given date is valid "
    else:
        return f"Given date is not valid "

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print(valid(y,m,d))
elif m==4 or m==6 or m==9 or m==11:
    print(valid_30(y,m,d))
elif m==2:
    print(valid_28(y,m,d))