'''Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?'''

'''
S(i,j)  = 1 if j = 0
        = S(i,j-1) + S(i-1,j) if 0 < j < i
        = 2 * S(i,j-1) if j == i

'''

import time

def routes(size):
    # start the route, assuming a cube, there is one router for each i,0 coordinate
    route = [1] * size

    for i in range(size):
        # now for each step, we need to count how many routes to (i,j) where j = i = = 2 * S(i,j-1), s(i,0) = 1
        for j in range(i):
            route[j] = route[j] + route[j-1]
        route[i] = 2 * route[i-1]
        print(route)
    return route

print(routes(20))
