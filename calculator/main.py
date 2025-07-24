def add(p,q):
    return p + q
def subtract(p, q):
    return p - q
def multiply(p, q):
    return p * q
def divide(p,q):
    return p/q

print("Welcome to the calculator!")
print(("a Add"))
print(("b Subtract"))
print(("c Multiply"))   
print(("d Divide"))
com=input("Please select an operation (a/b/c/d): ")
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

if com == "a":
    print(num1, "+", num2, "=", add(num1, num2))
elif com == "b":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif com == "c":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif com == "d":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid operation selected. Please choose a valid operation (a/b/c/d).")