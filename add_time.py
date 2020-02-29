# program to add two times
h1,m1,s1=input("Enter a 1st time with using : is ").split(":")
h2,m2,s2=input("Enter a 2nd time with using : is ").split(":")
s3=int(s1)+int(s2)
m3=int(m1)+int(m2)
h3=int(h2)+int(h1)
if s3>=60:
    m3=m3+s3//60
    s3=s3%60 
if m3>=60:
    h3+=m3//60
    m3=m3%60
print(f"Sum of 2 number :{h3}:{m3}:{s3}")
