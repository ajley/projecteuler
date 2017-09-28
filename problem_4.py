'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrone(x):
    str_x = str(x)
    if len(str_x) < 2:
        return True
    else:
        if str_x[0] == str_x[-1]:
            return isPalindrone(str_x[1:-1])

assert isPalindrone(123321)
assert isPalindrone('racecar')
assert  not isPalindrone('notapalindrone')

largest_palindrone = 0
x = 100
y = 100

for x in range(100,1000):
    for y in range(100,1000):
        if x*y > largest_palindrone and isPalindrone(x*y):
            largest_palindrone = x*y

print(largest_palindrone)
