"""
Exercise 3.2: Rewrite your pay program using try and except so that your
program handles non-numerical input gracefully by printing a message and
exiting the program. The following shows two executions of the program:
Enter Hours: 20
Enter Rate : nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
try:
    hours = float(input("Enter Hours: \n"))
    rate_per_hour = float(input("Enter rate per hour: \n"))
except:
    print("Error, please enter numeric input")
    quit()

if hours > 40:
    pay = (hours - 40) * rate_per_hour * 1.5 + 40 * rate_per_hour
else:
    pay = hours * rate_per_hour

print("Pay :", pay)
