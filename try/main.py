try:
    num=int(input("Enter a Number: "))
    print(num)
except Exception as ex:
    print("An exception occurred:", ex)
print("I am outside the try box:")