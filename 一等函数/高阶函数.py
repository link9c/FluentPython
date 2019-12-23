# 根据单词长度排序
fruits = ['apple', 'cherry', 'banana', 'fig']


def t1():
    print(sorted(fruits, key=len))


# 反序
def t2():
    def reverse(word):
        return word[::-1]

    print(sorted(fruits, key=reverse))


# python3 reduce函数
def t3():
    from functools import reduce
    from operator import add
    result = reduce(add, range(100))
    print(result)


if __name__ == '__main__':
    t1()
    t2()
    t3()
