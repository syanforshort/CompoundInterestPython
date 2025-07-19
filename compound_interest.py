# Defining the parameters
initial_deposit = float(input("What is your principal amount? "))
interest = float(input("What is the interest rate in decimal? "))
contribution = float(input("What is the amount of regular contribution? "))
compounding_type = input("What is the compounding type? Annual or Monthly? ").lower()
time_period_years = int(input("How many years is this good for? "))

# Type of compounding
if compounding_type == 'annual':
    number_compound = 1
elif compounding_type == 'monthly':
    number_compound = 12
else:
    print("Invalid. Try again.")

# Calculator
total_amount = initial_deposit * (1 + interest / number_compound) ** (number_compound * time_period_years)

total_contributions = contribution * (((1 + interest / number_compound) ** (number_compound * time_period_years) - 1) / (interest / number_compound))

final_amount = total_amount + total_contributions

print(f"{round(final_amount, 2)} is the final amount after {time_period_years} years.")
