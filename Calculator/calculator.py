print("---------------------Python Calculator---------------------")

# Looping the program

continue_calculating = True
while continue_calculating == True:
    number_valid = False
    while number_valid == False:

# Asking user for a value for "a" but making sure it's an actual number

        try:
            a = float(input("Enter a number: "))
            number_valid = True
        except ValueError:
            print("That's not a number...")

# Asking user for an operator but making sure it's an actual number

    operator_valid = False
    while operator_valid == False:
        operator = input("Enter a arithmetic operator (+ - / *): ")
        if operator == "+" or operator == "-" or operator == "/" or operator == "*":
            operator_valid = True
        else:
            print("Invalid operator. Please try again...")

# Asking user for a value for "b" but making sure it's an actual number

    number_valid = False
    while number_valid == False:
        try:
            b = float(input("Enter a number: "))
            number_valid = True
        except ValueError:
            print("That's not a number...")

# Numbers aren't divisible by 0

    if operator == "/" and b == 0:
        print("You can't divide this number by 0...") 
        continue

# Operator logic

    if operator == "+":
        answer = a + b
    elif operator == "-":
        answer = a - b
    elif operator == "/":
       answer = a / b
    elif operator == "*":
       answer = a * b
    else:
     print("You have entered something wrong.")
     exit()

# Formatted the "answer" variable so that it displays integers and floats seperately

    print(f"The answer is, {answer:g} ") 


 # Asking user if they want to calculate something again

    choice = input("Do you want to calculate again (y/n): ")

# loop logic
        
    while choice != "y" and choice != "n":
         print("Please enter y or n.")
         choice = input("Do you want to calculate again (y/n): ")

    if choice == "n":
        continue_calculating = False 

print("-----------------------------------------------------------")