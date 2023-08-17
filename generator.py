# A 'Generator' generates the required element of a sequence at run time (at the time when it is asked for)
# thus decreasing run-time overhead.
# If we do not use generators then we have to calculate the entire sequence at the beginning of the program
# even though we may not need all the elements of the sequence.


def GenerateCube(max_limit):
    for x in range(max_limit):
        yield x**3

values = GenerateCube(100)
# The memory size of the 'values' is always constant irrespecive of the given input of 'GenerateCube' function i.e., max_limit
# If you want to verify that then do:
# import sys
# print(sys.getsizeof(values))

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))


def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))