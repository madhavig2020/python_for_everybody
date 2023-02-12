"""
Exercise 4.6: Rewrite your pay computation with time-and-a-half for overtime
and create a function called computepay which takes two paramteters (hours and
rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""

def computepay(hours,rate_per_hour):
    if hours > 40:
        pay = (hours - 40) * rate_per_hour * 1.5 + 40 * rate_per_hour
    else:
        pay = hours * rate_per_hour
    #print("Pay :", pay)
    return pay

try:
    hours = float(input("Enter Hours: \n"))
    rate_per_hour = float(input("Enter rate per hour: \n"))
except:
    print("Error, please enter numeric input")
    quit()

pay = computepay(hours,rate_per_hour)
print("Pay:", pay)
