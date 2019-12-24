from functools import partial
from operator import mul

# 把原函数的某些参数固定
triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1, 10))))
