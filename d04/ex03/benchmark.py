import sys
import timeit
from functools import reduce

def f_loop(x):
    ret = 0
    for i in range(1, x + 1):
        ret += i * i
    return ret

def f_reduce(x):
    return reduce(lambda a, b: a + b * b, range(1, x + 1))

def benchmark():
    if len(sys.argv) == 4:
        if sys.argv[1] == 'loop':
            print(timeit.timeit(lambda: f_loop(int(sys.argv[3])), number=int(sys.argv[2])))
        if sys.argv[1] == 'reduce':
            print(timeit.timeit(lambda: f_reduce(int(sys.argv[3])), number=int(sys.argv[2])))
    else:
         Exception("incorrect arguments")

if __name__ == '__main__':
    benchmark()