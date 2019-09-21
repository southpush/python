def is_armstrong_number(number):
    number_len = len(str(number))
    count_list = [int(i) ** number_len for i in str(number)]
    return sum(count_list) == number

