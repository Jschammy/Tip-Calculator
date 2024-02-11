print("welcome to the tip calculator!\n")
bill_total = int(input("What was the total bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
tip = round(float(tip_percentage/100*(bill_total)),2)
total_num_people = int(input("How many people to split the bill?\n"))
bill_plus_tip = bill_total + tip
bill_per_person = "{:2f}".format(round(bill_plus_tip / total_num_people,2))
print(f"The total per person is ${bill_per_person}")
