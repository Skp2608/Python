print("This is an Keyboard Interrupt example using try & except keyword in python.\n")
while True:
    try:
        print("*Press CTRL+C to interrupt.")
        n=int(input("Enter a number to print it's square:"))
        print("\t-> Square of",n,"=",n**2,"\n")
    except KeyboardInterrupt:
        print("\n#Other key is pressed.\n")
