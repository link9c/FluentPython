import array
from collections import namedtuple

t = array.array('i', [12, 3, 4, 5])
print(t)

""" Return the tuple (x//y, x%y).  Invariant: div*y + mod == x. """
print(divmod(8, 4))

ll = namedtuple('name', 'a1 a2')

lat = ll(22, 33)
# 转成orderdict
print(lat._asdict())


if __name__ == '__main__':
    class A:
        print('a')

a = A()