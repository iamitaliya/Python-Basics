def CollatzRecursive(number):
    if number == 1:
        return 1
    elif number == 0:
        return 0
    elif number % 2 == 0:
        number = abs(number)/2
        print(int(number))
        return CollatzRecursive(number)
    elif number % 2 == 1:
        number = 3 * abs(number) + 1
        print(int(number))
        return CollatzRecursive(number)
    else:
        return 0


def CollatzIterative(number_to_iterate):
    number_to_iterate = abs(number_to_iterate)
    if number_to_iterate == 0:
        return 0
    while number_to_iterate > 1:
        if number_to_iterate % 2 == 0:
            number_to_iterate = number_to_iterate/2
            print(int(number_to_iterate))
        elif number_to_iterate % 2 == 1:
            number_to_iterate = 3 * number_to_iterate + 1
            print(int(number_to_iterate))


print(CollatzRecursive(-100))
print(CollatzIterative(-100))
