'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

number = 20
go = True
while go:
    if all(number % i == 0 for i in range(1,21)):
        print(number)
        go = False
    number += 20




