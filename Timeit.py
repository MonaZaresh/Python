# measure performance using the timeit module
# I need this library: brython_stdlib.js
import timeit

print('Performance and Timeit module')
# Experiment with sieve of Eratosthenes > find prime number with a certain range

def test1():
    [x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1]
    return(1)

def test2():
    [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]
    return(1)

def test3():
    # Initialize a list(empty list)
    primes = []
    for possiblePrime in range(2, 151):
    # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1): # square root
            if possiblePrime % num == 0:
                isPrime = False
                break # break the second for loop
        if isPrime:
            primes.append(possiblePrime)
    #print(primes)
    return(1)


# to find out which one is faster?
# timeit is a function inside the timeit module
# for using timeit module it's important that our methods/ functions have return value
# otherwise it's not gonna work
# timeit.timeit: print timestamps > how long this took
# ten cycles/iteration I want to run
print(timeit.timeit('test1()', globals=globals(), number=10)) # list comprehension 
print(timeit.timeit('test2()', globals=globals(), number=10))
print(timeit.timeit('test3()', globals=globals(), number=10))


# code that looks messay can very well be a lot faster than other code. 