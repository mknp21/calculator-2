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
#assigning num1 and num2
        operator = split_nums[0]
        num1 = split_nums[1]
        num2 = split_nums[2]
#         if the first token is "q":
        if operator == "q":
#             quit
            break
        if num1 != num1.isdigit() and num 2 != num2.isdigit():
            print("Sorry, that's not a valid entry!")
        # if the num parameters for each given operand is not an integer...
    # A place to store the return value of the math function we call,
    # to give us one clear place where that result is printed.
        result = None
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