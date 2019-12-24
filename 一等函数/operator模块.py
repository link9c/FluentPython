from functools import reduce
from operator import mul


# operator函数替代lambda函数
def fact(n):
    return reduce(mul, range(1, n + 1))


print(fact(10))
