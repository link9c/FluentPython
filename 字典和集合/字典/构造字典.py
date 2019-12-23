class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            print('====')
            raise KeyError(key)
        print('[]:%s' % self[str(key)])
        return self[str(key)]

    def get(self, key, default=None):

        try:
            print('get:%s' % self[key])
            # self[] 访问__missing__方法
            return self[key]

        except KeyError:
            print('get_d:%s' % default)
            return default

    def __contains__(self, key):
        print(key in self.keys() or str(key) in self.keys())
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    d['2']
    d[2]
    d.get(4)
    4 in d
