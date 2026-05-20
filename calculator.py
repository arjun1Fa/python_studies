'''

Asks the user for two numbers (they can be decimals).

Asks for an operator: +, -, *, /.

Performs the calculation and prints the result in a nice format (e.g., 5.0 + 3.0 = 8.0).

Handles division by zero (prints an error message instead of crashing).

'''


a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

choice = int(input("Enter the choice..\nEnter 1 for addition\nEnter 2 for substraction\nEnter 3 for multiplication\nEnter 4 for division\nEnter 5 to exit\n"))
result = None


if choice == 1 :
    result = a+b
elif choice == 2 :
    result = a-b
elif choice == 3 :
    result = a*b
elif choice == 4 :
    if b == 0:
        print("Invalid operation")
    else :    
      result = a/b

elif choice == 5 :
       print("Ending program")
       exit

print("The final answer is ", result)
    