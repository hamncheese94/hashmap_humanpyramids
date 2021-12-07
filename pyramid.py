'''
Project 6: Hashing and Caching
Author: Christian Alexander
Created: 11/21/21
Course: CS2420
Purpose: find weight each person supports of a human pyramid given sys.argv[1]
'''

import sys
from time import perf_counter
from hashmap import HashMap
cache={}
function_calls = 0
cache_hits = 0
# recursive function; finds weight for r,c
def weightOn(r,c):
    global function_calls
    global cache_hits
    function_calls += 1
    if (r,c) in cache:
        cache_hits += 1
        return cache[(r,c)]
    weight = 0
    if r == 0 and c == 0:
        return weight
    if c == 0:
        weight = (weightOn(r-1,0) + 200) / 2.0
    elif c == r:
        weight = (weightOn(r-1,r-1) + 200) / 2.0
    else:
        left = (weightOn(r-1,c-1) + 200) / 2.0
        right = (weightOn(r-1,c) + 200) / 2.0
        weight = left + right
    cache[(r,c)] = weight
    return weight
# loops weightOn for sys.argv[n] ... n levels
def main():
    global function_calls
    global cache_hits
    rows = int(sys.argv[1])
    startTime = perf_counter()
    for r in range(0, rows):
        for c in range(0, r+1):
            print('{0:.2f}'.format(weightOn(r,c)), end=' ')
        print()
    endTime = perf_counter()
    elapsedTime = endTime - startTime
    print('Elapsed time: ', elapsedTime, 'seconds')
    print('Number of function calls: ', function_calls)
    print("Number of cache hits: ", cache_hits)

    x = function_calls
    y = cache_hits
# redirects output to 'part3.txt' as a seperate loop to preserve function_calls count'
    sys.stdout = open('part3.txt', 'w')
    function_calls = 0
    cache_hits = 0
    for r in range(0, rows):
        for c in range(0, r+1):
            print('{0:.2f}'.format(weightOn(r,c)), end=' ')
        print()
    print('Elapsed time: ', elapsedTime, 'seconds')
    print('Number of function calls: ', x)
    print("Number of cache hits: ", y)
    sys.stdout.close()


if __name__ == '__main__':
    main()
