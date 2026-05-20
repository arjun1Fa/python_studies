'''Ask the user for the radius of a circle (can be a decimal).

Calculate and display the circle's area and circumference using math.pi.

Area = π × radius²

Circumference = 2 × π × radius

Round each result to 2 decimal places using round().

Ask the user for a score (0 to 100).

Determine the letter grade using if-elif-else:

90–100: A

80–89: B

70–79: C

60–69: D

below 60: F

(Assume input is valid for now.)

Print a final summary like this (use f-strings):

text
Circle radius: 5.0
Area: 78.54
Circumference: 31.42
Your score: 85
Grade: B
'''
import math

radius = int(input(" Enter the radius of the circle: " ))
area = math.pi * math.pow(radius , 2)
circumference = 2*math.pi*radius
round(area , 2)
round(circumference, 2)
print("\nThe area of the circle is :", area)

score = int(input("\nEnter a score of your choice : "))

if score <= 100 && if score
