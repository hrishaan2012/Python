def convertobinary(n):
    if n > 1:
        convertobinary(n // 2)
    print(n % 2, end='')

dec=float(input("Enter a number to convert into binary:"))

convertobinary(dec)
print() 