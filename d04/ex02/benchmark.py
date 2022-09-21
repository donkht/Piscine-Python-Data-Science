import sys
import timeit

def f_loop():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    gmails = []
    for x in emails:
        if (x.find('@gmail.com') > 0):
            gmails.append(x)
    return gmails

def f_comprehension():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    return [x for x in emails if x.find('@gmail.com') > 0]

def f_map():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    return list(map(lambda x: x if x.find('@gmail.com') > 0 else None, emails))

def f_filter():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    return filter(lambda x: x if x.find('@gmail.com') > 0 else None, emails)

def benchmark():
    if len(sys.argv) == 3:
        if sys.argv[1] == 'loop':
            print(timeit.timeit(setup=f_loop, number=int(sys.argv[2])))
        if sys.argv[1] == 'list_comprehension':
            print(timeit.timeit(setup=f_comprehension, number=int(sys.argv[2])))
        if sys.argv[1] == 'map':
            print(timeit.timeit(setup=f_map, number=int(sys.argv[2])))
        if sys.argv[1] == 'filter':
            print(timeit.timeit(setup=f_filter, number=int(sys.argv[2])))
        else:
            print("incorrect argument")
    else:
         Exception("incorrect arguments")

if __name__ == '__main__':
    benchmark()