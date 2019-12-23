import collections


class StrKeyDict0(collections.UserDict):
    # 找不到key的时候才会调用
    def __missing__(self, key):
        if isinstance(key, str):
            print('====')
            raise KeyError(key)
        print('[]:%s' % self[str(key)])
        return self[str(key)]

    def __setitem__(self, key, value):
        print('set:%s' % value)
        self.data[str(key)] = value

    def __contains__(self, key):
        print(str(key) in self.data)
        return str(key) in self.data


if __name__ == '__main__':
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    d[2]
    print(d['2'])
    d.get(4)
    4 in d
