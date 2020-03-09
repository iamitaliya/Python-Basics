# armstrong number
def is_armtrong(num):
    str_num = str(num)
    sum_of_num = 0
    for integer in str_num:
        integer = int(integer) ** len(str_num)
        sum_of_num += integer

    return sum_of_num == num


print(is_armtrong(153))
