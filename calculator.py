"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
    # creating list with math options
math_options = ["+", "-", "*", "/", "s", "c", "p", "m"]
# repeat forever:
while True:
#     read input
    enter_nums = input("> ")
#     tokenize input
    split_nums = enter_nums.split(' ')
    if len(split_nums) < 3:
        num2 = 0
    if len(split_nums) < 2:
        print("Enter more inputs!")
        continue
    else: 
        num2 = int(split_nums[2])
        num1 = int(split_nums[1])

    # if 2 < len(split_nums) < 3:
    #     num1 = 0
    #     num2 = 0
    # if len(split_nums) == 3:
    #     num2 = int(split_nums[2])
        
    # if len(split_nums) < 2: 
    #     print("Not valid input!")
#assigning num1 and num2
    
    operator = split_nums[0]
    num1 = int(split_nums[1])
# to give us one clear place where that result is printed.
    result = None
#         if the first token is "q":
    if operator == "q":
#             quit
        break
    #check if operator is valid
    if operator not in math_options:
        print("Sorry, not a valid operator.")
    # if the num parameters for each given operand is not an integer...    
    # if num1 != num1.isdigit() and num2 != num2.isdigit():
    #     print("Sorry, that's not a valid entry!")
# A place to store the return value of the math function we call,
#        (decide which math function to call based on first token)
#        if the first token is 'pow':
    elif operator == "+":   
#            call the power function with the other two tokens
        result = add(float(num1), float(num2))
    elif operator == "-":
        result = subtract(float(num1), float(num2))
    elif operator == "*":
        result = multiply(float(num1), float(num2))
    elif operator == "/":
        result = divide(float(num1), float(num2))
    elif operator == "s":
        result = square(float(num1))
    elif operator == "c":
        result = cube(float(num1))
    elif operator == "p":
        result = power(float(num1))
    elif operator == "m":
        result = mod(float(num1), float(num2))
    
    print(result)