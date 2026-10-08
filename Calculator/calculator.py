print("---------------------Python Calculator---------------------")

continue_calculating = True
while continue_calculating == True:
    try:
        a = float(input("Enter a number: "))
    except ValueError:
        print("That's not a number...")
        exit()
    
    operator = input("Enter a arithmetic operator (+ - / *): ")


    try:
        b = float(input("Enter a number: "))
    except ValueError:
        print("That's not a number...")
        exit()

    if operator == "/" and b == 0:
        print("You can't divide this number by 0...")#
        exit()
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
    
    print(f"The answer is, {answer:g} ") # Formatted the "answer" variable so that it displays integers and floats seperately

    choice = input("Do you want to calculate again (y/n): ") # Asking user if they want to calculate something again
    if choice == "n":
        continue_calculating = False
        

print("-----------------------------------------------------------")