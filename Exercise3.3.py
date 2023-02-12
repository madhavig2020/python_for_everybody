"""
Exercise 3.3Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and
1.0, print a grade using the following table:
Score    Grade
>= 0.9      A
>= 0.8      B
>= 0.7      C
>= 0.6      D
< 0.6      F
~~~
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly as shown above to test the various, different
values for input.

"""
try:
    grade = float(input("Enter Score: "))
except:
    print("Bad score")
    quit()

if grade < 0 or grade > 1.0:
    print("Enter  score between 0.0 and 1.0")
elif grade >= 0.9:
    print("A Grade")
elif grade >= 0.8:
    print("B Grade")
elif grade >= 0.7:
    print("C Grade")
elif grade >= 0.6:
    print("D Grade")
else:
    print("F Grade")
