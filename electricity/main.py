units=int(input("Enter the electricity units used :"))

if units < 50:
    amount=units*2 
    subcharge=25

elif units <100 :
    amount=55+(units-50)*3
    subcharge=35

elif units < 200:
    amount=155+(units-100)*5
    subcharge=55

else:

    amount=255+(units-200)*7
    subcharge=85

total=amount+subcharge
print("Elecricity Bill = ", total)