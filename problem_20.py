'''n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


def factorial(x):
    res = 1
    while x > 1:
        res *= x
        x -= 1
    return res


def sumDigits(x):
    res = 0
    xStr = str(x)
    for char in xStr:
        res += int(char)
    return res

print(sumDigits(factorial(100)))