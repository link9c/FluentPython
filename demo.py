class A(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(self.a)

    def add_(self):
        print('aaa')
        return self.a + self.b


b = B(2,3)
b.add_()

