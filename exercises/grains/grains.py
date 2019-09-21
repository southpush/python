def square(number):
    if not 1 <= number <= 64:
        raise ValueError("error range")
    return pow(2, number - 1)


def total(number):
    if not 1 <= number <= 64:
        raise ValueError("error range")
    return pow(2, number) - 1

