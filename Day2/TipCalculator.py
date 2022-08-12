# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line
print("Welcome to the tip calc")

bill = float(input("What is the total bill amount? "))
tipPerc = float(
    input("What percentage tip would you like to give? 10,15,20? "))
numPeople = int(input("How many people are splitting the bill? "))

totalBill = (bill * ((100+tipPerc)/100))

amount = round((totalBill/numPeople), 2)

print(f"Each person should pay {amount}")
