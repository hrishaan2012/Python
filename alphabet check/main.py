c= input("Enter a character: ")
if len(c)>1:
    print("Invalid input")
else:
    if c>="a" and c<="z":
        print("This chartacter is a alphanbet")

    elif c>="A" and c<="Z":
        print("This character is a capital alphabet")
    else:
        print("This character is not an alphabet")