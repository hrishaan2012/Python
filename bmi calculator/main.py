weight=float(input("Enter the weight in kg: "))
height=float(input("Enter the height in cm: "))
bmi=weight/(height/100)**2
print("Your BMI is:", bmi)
if bmi < 18.5:
    print("Underweight")    
elif 18.5 <= bmi < 24.9:
    print("Healthy weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obesity")