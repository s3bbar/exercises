multiplier = 4
has_calculated = False


def multiply_calculator(number):
    global has_calculated
    has_calculated = True
    result = number * multiplier
    return result


print(multiply_calculator(10))
print(has_calculated)
