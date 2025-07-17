num=int(input("Enter Your Number:"))
count=0
while num!= 0:
    count+=1
    num//=10
    print("Number of Digits:", count)     
    