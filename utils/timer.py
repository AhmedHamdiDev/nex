import time

def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    print(f"\nExecution time: {round(end - start, 4)} seconds")
