'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

res = 0
primes = []
number = 600851475143
upper = number ** 0.5 + 1
i = 1


def isPrime(x):
    if x % 2 == 0 or x < 3:
        return False
    else:
        for i in range(3, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True


assert isPrime(5)
assert not isPrime(4)

while i < upper:
    if number % i == 0 and isPrime(i):
        primes.append(i)

    i += 1

print(max(primes))

