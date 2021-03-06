from math import hypot


class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __abs__(self):
        # 欧式距离
        return hypot(self.x, self.y)

    # 若不存在x.__bool__()则尝试调用x.__len__()
    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(2, 3)
    print(abs(v1))
    print(v1 + v2)
    print(v1 * 3)
    print(bool(v1))
