'''Asks the user to enter a weight with its unit in one line, like 70 kg or 150 lbs.

Uses .strip() and .split() to separate the numeric value from the unit.

Converts the weight to the other unit:

kg → lbs: multiply by 2.20462

lbs → kg: multiply by 0.453592

Prints the result rounded to 2 decimal places, in a friendly format.

If the unit is not recognised (something other than kg/kilos/kilogram or lb/lbs/pounds), print an error'''


user_input = input("Please enter your weight: ")

weight , metric = user_input.split()
weight = float(weight)

if metric == "kg" or metric == "kilo" or metric == "k" :
    weight1 = weight*2.204621
    metric2 = "Lbs"
elif metric == "lbs" or metric == "pounds" or metric == "lb":
    weight1 = weight * 0.453592
    metric2 = "Kg"
else:
        print("\nUnidentified metric")
        exit

weight = round(weight,2)

print("The weight of the user is ", weight,metric ," and in " ,metric2, " is ", weight1 , metric2)