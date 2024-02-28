""" pseudocode
display the text "investment - to calculate the amount of interest you'll earn on your investment \n
                  bond - to calculate the amount you'll have to pay on a home loan"
ask user to input either "investment" or "bond", convert to lowercase and store as variable "selection"
if "selection" = "investment":
    ask user to input the amount of money they're depositing, store as variable "deposit"
    ask user to input interest rate as percentage, convert to decimal and store as variable "rate"
    ask user to input the number of years they plan on investing, store as "time_years"
    ask user to input selection of "simple" or "compound", convert to lowercase and store as "interest_type"
    if "interest_type" = "simple":
        calculate total using "total" = "deposit" * (1 + (("rate"/100) * time_years))
        print "total"
    if "interest_type" = "compound":
        calculate total using "total" = "deposit" * math.pow((1 + "rate", "time_years")
        print "total"
if "selection" = "bond":
    ask user to input present value of the house, store as variable "house_value"
    ask user to enter the interest rate as percentage, convert to decimal and store as "rate"
    ask user to enter number of months they plan to take to repay bond, store as "time_months"
    calculate monthly repayment, "monthly_repayment" = ((rate)/12) * house_value) / (1 - (1 + (rate/12)**(-"time_months"))
    print "repayment"
"""

import math

print("\ninvestment\t- to calculate the amount of interest you'll earn on your investment \nbond\t\t- to calculate the amount you'll have to pay on a home loan\n") # Prints description of options.
selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() # Asks user to choose option, makes input lowercase.

if (selection == "investment"): # If condition is true, requests following inputs to calculate investment return.
    deposit = float(input("\nHow much money will you deposit? "))
    rate = float(input("What is your interest rate (as a percentage)? ")) / 100 # Asks for rate and converts from percentage to decimal number (also converts from str to float).
    time_years = int(input("How many years do you plan on investing for? "))
    interest_type = input("\nTo select simple interest, type 'simple'\nTo select compound interest, type 'compound': ").lower() # Asks user to choose interest type, makes input lowercase.

    if (interest_type == "simple"):
        total = round(deposit * (1 + (rate * time_years)), 2) # Calculates total with simple interest and rounds to 2 decimal points.
        print(f"\nAfter {time_years} years, your investment will be worth: {total}\n") # Prints result.
    elif (interest_type == "compound"):
        total = round(deposit * math.pow((1 + rate), time_years), 2) # Calculates total with compound interest and rounds to 2 decimal points.
        print(f"\nAfter {time_years} years, your investment will be worth: {total}\n") # Prints result.
    else:
        print("\nThat didn't work! Please try again.\n") # Prints error message.

elif (selection == "bond"): # If condition is true, requests following inputs to calculate monthly repayment on bond.
    house_value = float(input("\nWhat is the value of the house? "))
    rate = float(input("What is your interest rate (as a percentage)? ")) / 100 # Asks for rate and converts from percentage to decimal number (also converts from str to float).
    time_months = int(input("Over how many months do you plan to repay the bond? "))
    monthly_repayment = round(((rate / 12) * house_value) / (1 - (1 + (rate / 12)) ** (-time_months)), 2) # Calculates monthly repayment and rounds to 2 decimal points.
    print(f"\nYour monthly bond repayments will be: {monthly_repayment}\n") # Prints result.
else:
    print("\nThat didn't work! Please try again.\n") # Prints error message.

