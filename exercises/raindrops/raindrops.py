def convert(number):
    return (
            f"{ 'Pling' if number % 3 == 0 else ''}"
            f"{ 'Plang' if number % 5 == 0 else ''}"
            f"{ 'Plong' if number % 7 == 0 else ''}"
            f"{ number if number % 3 != 0 and number % 5 != 0 and number % 7 != 0 else ''}"
    )
