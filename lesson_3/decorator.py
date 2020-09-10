import time


def timer(num):

    def decor_func(func):

        def wrapper():
            full_run_time = 0
            result = 0
            for _ in range(num):
                start_time = time.perf_counter()
                value = func()
                end_time = time.perf_counter()
                run_time = end_time - start_time
                full_run_time += run_time
                result = value
                print(f"Function took {run_time: .6f} seconds to complete.")

            print(f"Total time = {full_run_time: .6f}\nFunction {func.__name__!r}")
            print(f"Last result = {result}")
            return result

        return wrapper

    return decor_func


@timer(10)
def waste_time():
    total = 0
    for i in range(10000):
        total += 1
    return total


time_result = waste_time()
