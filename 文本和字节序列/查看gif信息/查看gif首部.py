import struct

# <小字节序;3s3s两个3字节序列;HH是两个16位二进制整数
fmt = '<3s3sHH'
with open('test.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))
print(struct.unpack(fmt, header))
