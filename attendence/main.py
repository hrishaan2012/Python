a=input ("Did you had any medical condition Y or N:")
x=int(input("What is your attendence percent: "))

if a=="Y":
    print("You are eligible for the exam")
else :
    if x>=75:
        print("You are eligible for the exam")
    else:
        print("You are not eligible for the exam")

