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


def benchmark():
    t1 = timeit.timeit(setup=f_loop, number=90000000)
    t2 = timeit.timeit(setup=f_comprehension, number=90000000)
    t3 = timeit.timeit(setup=f_map, number=90000000)
    t = (t1, t2, t3)
    t = tuple(sorted(t))

    if t[0] == t3:
        print('it is better to use a map')
    elif t[0] == t2:
        print('it is better to use a list comprehension')
    if t[0] == t1:
       print('it is better to use a loop')
    print(str(t[0]) + ' vs ' + str(t[1]) + ' vs ' + str(t[2]))

if __name__ == '__main__':
    benchmark()