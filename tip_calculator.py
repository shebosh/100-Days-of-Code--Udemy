print("Welcome to the tip calculator!")
print("This program will help you calculate the amount each person should pay, including the tip")
bill = int(input("Enter the amount in $: "))
people = int(input("How many people are paying the bill? "))
tip = 12 / 100 * bill

total = bill + tip

pay_bill = total / people

print(pay_bill)
