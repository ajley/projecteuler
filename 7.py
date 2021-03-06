'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

def isPrime(x):
    if x % 2 == 0:
        return False
    else:
        for i in range(3,int(x**0.5)+1):
            if x % i == 0:
                return False

    return True

primes = [2]
i = 3
while len(primes) < 10001:
    if isPrime(i):
        primes.append(i)
    i += 1
print(primes[-1])
