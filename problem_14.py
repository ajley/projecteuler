'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''
import time

def sequenceRules(x):
    if x % 2 == 0:
        return x//2
    else:
        return 3 * x + 1

starttime = time.time()
done = {}
max_count = 0
res = 0
for i in range(1000000):

    start = i
    count = 1

    while i > 1:
        count += 1
        if i in done.keys():
            count += done[i]
            break
        else:
            i = sequenceRules(i)
    done[start] = count
    if count > max_count:
        max_count = count
        res = start


print(res,max_count)
endtime = time.time()
print("{0:.2f} seconds".format(endtime-starttime))
