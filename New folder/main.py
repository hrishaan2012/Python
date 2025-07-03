string=input("Enter a word:")

string2=("")

for i in string:
    string2= i + string2

print("Orignal word :", string)
print("\nReversed word:", string2)