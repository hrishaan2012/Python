n=int(input("Enter the number of items:"))

price=2.50
def calculate_change(amount_given):
    return amount_given - price
c=calculate_change(4.00)
p=c*n
print("Change to be returned: ",p)