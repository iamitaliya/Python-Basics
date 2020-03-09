def GreatestCommonDivisor(number1, number2):
    if number1 == 0 or number2 == 0:
        return 0
    else:
        while number2 > 0:
            temp_num = number1 % number2
            number1 = number2
            number2 = temp_num

    return number1


print(GreatestCommonDivisor(9, 10))
