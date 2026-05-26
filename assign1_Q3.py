customer_name = input("Enter Customer Name: ")
unit = int(input("Enter Units Consumed: "))

if (unit <= 100):
    bill = unit * 5
else:
    bill = (100 * 5) + ((unit - 100) * 18)

print("ELECTRICITY BILL RECEIPT")
print(f"Customer Name: {customer_name}")
print(f"Units Consumed: {unit}")
print(f"Total Bill: Rs. {bill}")    