"""
Exercise 4.7: Rewrite the grade program from previous chapter using a function
called computegrade that takes a score as its parameter and returns a grade as
a string.
Score    Grade
>= 0.9      A
>= 0.8      B
>= 0.7      C
>= 0.6      D
< 0.6      F
~~~
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly  to test the various, different values for input.
Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
def computegrade(score):
    if score < 0 or score > 1.0:
        return ("Enter  score between 0.0 and 1.0")
    elif score >= 0.9:
        return ("A Grade")
    elif score >= 0.8:
        return ("B Grade")
    elif score >= 0.7:
        return ("C Grade")
    elif score >= 0.6:
        return ("D Grade")
    else:
        return ("F Grade")

try:
    score = float(input("Enter Score: "))
except:
    print("Bad score")
    quit()

print(computegrade(score))
