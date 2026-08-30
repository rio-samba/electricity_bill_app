

amount = 0

no_of_meter = 0

curr_units_list = []
prev_units_list = []

total_units = []

sum_total_units = 0

total_bills = []



amount = int(input("Enter Amount : "))
print(amount)

no_of_meter = int(input("Enter no of Meters :"))
print(no_of_meter)


for i in range(no_of_meter):
    curr_meter_unit = int(input(f"Enter Current Unit of Meter no {i+1} :"))
    curr_units_list.append(curr_meter_unit)

    prev_meter_unit = int(input(f"Enter Previous Unit of Meter no {i+1} :"))
    prev_units_list.append(prev_meter_unit)


for i in range(no_of_meter):
    unit_n = curr_units_list[i] - prev_units_list[i]
    total_units.append(unit_n)


print(f"Total units after subtraction are : {total_units}")

sum_total_units = sum(total_units)

print(f"Total unit sum : {sum_total_units}")


avg_units_price = amount/sum_total_units
print(f"Average Unit Price : {avg_units_price}")


for i in range(no_of_meter):
    bill = avg_units_price * total_units[i]
    total_bills.append(bill)


print("Bill of each Meters are : ")
for i in range(no_of_meter):
    print(f"Meter {i+1} : Taka {total_bills[i]}")
