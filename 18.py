'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67,
is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires
 a clever method! ;o)

'''

# Re-think the problem and work bottom up -  largest number atfer layer n = layer[n-1] + 'layer[n]' - So add largest
# available from layerN and add to layer n-1. if layer len == 1, stop.

numbers = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

numbers = numbers.split("\n")
numsA = []
for row in numbers:
    numsA.append([int(num) for num in row.split(" ")])

numsB = [x[:] for x in numsA]


def bottomUpRoute(grid):
    startingLevel = len(grid)

    if len(grid[startingLevel-1]) == 1:
        return grid[startingLevel-1]
    else:
        for i in range(len(grid[startingLevel-2])):
            grid[startingLevel-2][i] = grid[startingLevel-2][i] + max(grid[startingLevel-1][i],grid[startingLevel-1][i+1])
        nextgrid = grid[:-1]
        #print(nextgrid)
        return bottomUpRoute(nextgrid)


def bottomUpRoute2(grid):
    level = len(grid) - 2
    while level >= 0:
        for i in range(len(grid[level])):
            grid[level][i] = grid[level][i] + max(grid[level+1][i],grid[level+1][i+1])
        level -= 1
    return (grid[0])

print(bottomUpRoute(numsA)[0])
print(bottomUpRoute2(numsB)[0])



