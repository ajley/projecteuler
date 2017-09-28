'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''

a = 1
b = 1
go = True

while go:
    for b in range(a, 1000):
        if (a ** 2 + b ** 2) ** 0.5 == 1000 - (a + b):
            print(a*b*int((a ** 2 + b ** 2) ** 0.5))
            go = False
            break
    a += 1
