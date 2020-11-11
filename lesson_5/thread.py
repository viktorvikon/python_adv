from threading import Thread
import time


def threads(thread_name, is_daemon):

    def actual_decorator(func):

        def wrapper(*args):
            new_thread = Thread(target=func, args=args, name=thread_name, daemon=is_daemon)
            new_thread.start()
            return new_thread

        return wrapper

    return actual_decorator


@threads('Thread', False)
def range_function():
    a = time.time()
    time.sleep(1)
    for i in range(10):
        print(i)
    print(time.time() - a)


range_function()
