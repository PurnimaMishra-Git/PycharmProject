import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("some work need to done")
    some_work(3)
    print("some work after 3 sec")
    some_work(3)
    print("someworkdone")
