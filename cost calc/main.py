def total_calc(bill_amount, tip_percentage):
    total= bill_amount *(1+ 0.1* tip_percentage / 100)
    total = round(total, 2)
    print(f"The total amount is: Rs {total}")
total_calc(150,20)

