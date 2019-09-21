# def factors(value):
#     results = []
#     divisor = 2
#     count = 0
#     while divisor <= value:
#         count += 1
#         if value % divisor == 0:
#             results.append(divisor)
#             value = value / divisor
#         else:
#             divisor += 1
#     print(count)
#     return results
#

def factors(value):
    count = 0
    prime = 2
    prime_factors = []

    while not value == 1:
        count += 1
        if value % prime == 0:
            value /= prime
            prime_factors.append(prime)
        else:
            prime += 1
    print(count)
    return prime_factors


factors(45)