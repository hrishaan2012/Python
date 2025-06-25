sp=int(input("Enter The SP"))
cp=int(input("Enter The CP"))

if sp>cp:
    p=sp-cp
    print("Profit is ",p)
else:
    l=cp-sp
    print("Loss is",l)