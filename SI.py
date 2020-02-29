P, T, R = input("Enter a Principle , Time , Rate ").split()
P = int(P)
T = int(T)
R = int(R)

def SI1(P, T, R):
    SI = (P*T*R)/100
    return SI

print(f"Simple Interest is {SI1(P,T,R)}")
