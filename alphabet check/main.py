y= int(input("Enter the money with you"))
c= int(input("Enter the maximum apples you can eat"))
p= int(input("Enter the price of one apple"))
sp= y/p
if sp > c:
    print("You can eat only", c, "apples")
else:
    print("You can eat", sp, "apples")
if sp == 0:
    print("You can't eat any apples")
else:
    print("You can eat apples")