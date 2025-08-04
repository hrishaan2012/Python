valid=False

while not valid:
    try:
        n=int(input("Enter a integer: "))
        while n%2 == 0:
           
            print("meow meow meow meow")
            valid=True
    except ValueError:
        print("Invalid input. Please enter an integer.")