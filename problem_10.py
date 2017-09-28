'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''

def isPrime(x):
    if x % 2 == 0:
        return False
    else:
        for i in range(3,int(x**0.5)+1):
            if x % i == 0:
                return False

    return True

sumPrimes = 2
i = 3
while i < 2000000:
    if isPrime(i):
         sumPrimes += i
    i += 2
print(sumPrimes)
