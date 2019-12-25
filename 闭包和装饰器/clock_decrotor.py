import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        # 返回性能计数器的值（以分秒为单位），即具有最高可用分辨率的时钟，以测量短持续时间
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

if __name__ == '__main__':
    factorial(10)
