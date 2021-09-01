"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# repeat forever:
    while True:
#     read input
        enter_nums = input("> ")
#     tokenize input
        split_nums = enter_nums.split(' ')
#         if the first token is "q":
        if split_nums[0] == "q":
#             quit
                break

    # A place to store the return value of the math function we call,
    # to give us one clear place where that result is printed.
        result = None
#        (decide which math function to call based on first token)
#        if the first token is 'pow':
        elif split_nums[0] == "+":   
#            call the power function with the other two tokens
            result = add(float(num1), float(num2))git