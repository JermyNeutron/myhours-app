import time


def timelap(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_stop = time.time()
        print(f"Lap for {func.__name__}: {(time_stop - time_start):.4f}s")
        return result
    return wrapper
