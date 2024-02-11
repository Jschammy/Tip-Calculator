print("Welcome to the tip calculator!")
print(f"-"*30)
#variables and user inputs
bill = float(input("What is your bill?\n"))
tip_percentage = int(input("What percentage tip are you giving? 10, 12, 15, or 20\n"))
tip = tip_percentage / 100 * (bill)
bill_total = bill + tip
people_total = int(input("How many people are splitting the bill?\n"))
bill_per_person = bill_total / people_total
final_bill = round(bill_per_person, 2)
print(f"-"*30)
#final output to user
print(f"The bill per person is: ${final_bill}")

