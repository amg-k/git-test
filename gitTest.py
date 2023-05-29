from random import randint

def num_sum(num1, num2):
    return num1 + num2


def num_multiple(fix1, fix2):
    return fix1 * fix2

def circle_area_calc(radius):
    return 3.14 * radius ** 2

def return_random(start, end):
    return randint(start, end)

print(num_sum(28, 18))
print(num_multiple(14, 18))
print("Area of circle is: ", circle_area_calc(8))
print(return_random(1, 11))

print(num_sum(81, 184))
