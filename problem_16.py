'''215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?'''

def powerOf(x):
    return 2**x

def sumChars(x):
    res = 0
    for char in str(x):
        res += int(char)
    return res

print(sumChars(powerOf(1000)))