"""
LRU:Least Recently Used
"""

from 闭包和装饰器 import clock_decrotor
# import clock_decrotor
import functools


# lru_cache装饰的参数必须可散列
@functools.lru_cache()
@clock_decrotor.clock
def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':
    print(fib(30))
