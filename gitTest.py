from random import randint

def num_sum(num1, num2):
    return num1 + num2


def num_multiple(num1, num2):
    return num1 * num2

def area_calc(side1, side2):
    return side1 * side2

def return_random(start, end):
    return randint(start, end)

print(num_sum(28, 18))
print(num_multiple(14, 18))
print("Area of rectangle is: ", area_calc(8, 4))
print(return_random(1, 11))
