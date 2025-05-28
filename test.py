import time
def timeit(func):
    def wrapper():
        s=time.time()
        func()
        print(f"{func.__name__}時間為:{time.time()-s}")
    return wrapper

@timeit
def sleep_1():
    time.sleep(1)

sleep_1()