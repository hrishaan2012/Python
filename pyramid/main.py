print("Half Pyramid of *pattern")
n=int(input("Enter the number of rows"))

for i in range (n):
    for j in range(i+1):
     if ( j <= n-1):
        print("", end=" ")
    else:
        print("*", end=" ")
    print() 