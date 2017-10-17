'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.'''
import string as str

numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

def num2Word(x):
    if x in numbers.keys():
        return numbers[x]
    elif x < 100:
        ones = x%10
        tens = x - ones
        return numbers[tens] + "-" + numbers[ones]
    elif x < 1000:
        remainder = x % 100
        hundreds = (x - remainder) // 100
        if remainder in numbers.keys():
            return numbers[hundreds] + " hundred and " + numbers[remainder]
        elif remainder == 0:
            return numbers[hundreds] + " hundred"
        else:
            ones = remainder % 10
            tens = remainder - ones
            return numbers[hundreds] + " hundred and " + numbers[tens] + "-" + numbers[ones]
    elif x < 10000:
        remainder = x % 1000
        thousands = (x - remainder) // 1000
        if remainder in numbers.keys():
            return numbers[thousands] + " thousand and " + numbers[remainder]
        elif remainder == 0:
            return numbers[thousands] + " thousand"
        else:
            remainder2 = remainder % 100
            hundreds = (remainder - remainder2) // 100
            if remainder2 in numbers.keys():
                return numbers[thousands] + " thousand " + numbers[hundreds] + " hundred and "+ numbers[remainder2]
            elif remainder2 == 0:
                return numbers[thousands] + " thousand " + numbers[hundreds] + " hundred"
            else:
                ones = remainder2 % 10
                tens = remainder2 - ones
                return numbers[thousands] + " thousand " + numbers[hundreds] + " hundred and " + numbers[tens] + "-" + numbers[ones]
    else:
        return "number not catered for"


print(num2Word(9999))

letters = str.ascii_lowercase
res = 0
for i in range(1,1001):
    text = num2Word(i)
    print(text)
    for char in text:
        if char in letters:
            res += 1
print(res)
