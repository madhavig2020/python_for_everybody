# Exercise 3.1
"""
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly.
"""

# prompt user for hours
#  prompt user for rate per hour
# compute gross pay  hours*rate per hour
# 0-40 hrs = pay
# more than 40 - 1.5 times

hours = float(input("Enter Hours: \n"))
rate_per_hour = float(input("Enter rate per hour: \n"))

if hours > 40:
    pay = (hours - 40) * rate_per_hour * 1.5 + 40 * rate_per_hour
else:
    pay = hours * rate_per_hour

print("Pay :", pay)
