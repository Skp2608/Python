import math
P, T, R = input("Enter a Principle , Time , Rate ").split()
P = int(P)
T = int(T)
R = float(R)


def SI1(P, T, R):
    SI = P*pow(1+(R/100), T)
    return SI


print(f"Compound Interest is {SI1(P,T,R)}")
