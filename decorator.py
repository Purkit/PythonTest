import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        function(*args, **kwargs)
        after = time.time()
        time_elapsed = after - before
        name_of_funtion = function.__name__
        print(f"Function \"{name_of_funtion}\" took {time_elapsed} sec to finish execution!")
    return wrapper

@timed
def some_test_function(x):
    result = 1
    for i in range(1, x):
        result *= i
    # return result

some_test_function(1000)