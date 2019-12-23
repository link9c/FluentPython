import collections
ct = collections.Counter('abcdeeaa')
print(ct)
ct.update('aaa')
print(ct)
print(ct.most_common(2))
