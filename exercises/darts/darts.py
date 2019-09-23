def score(x, y):
    distance = x ** 2 + y ** 2
    return 10 if distance <= 1 ** 2 else 5 if distance <= 5 ** 2 else 1 if distance <= 10 ** 2 else 0
