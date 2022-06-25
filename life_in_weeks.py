age = int(input("What is your current age?"))

remaining_time = 90 - age

days = 365
weeks = 52
months = 12

remaining_days = remaining_time * days
remaining_weeks = remaining_time * weeks
remaining_months =remaining_time * 12

print(f"You are {age} years old and you have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left to live until 90." )