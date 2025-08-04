try:
    num1=int(input("Enter a number :"))
    num2=int(input("Enter another number :"))
    result = num1 / num2
    print ("The result is:", result)
except ValueError:
    print("Invalid input! Please enter valid integers.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except Exception as ex:
    print("An unexpected error occurred:", ex)
finally:
    print("I will execute no matter what happens.")