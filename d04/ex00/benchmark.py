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

    
def benchmark():
    t1 = timeit.timeit(setup=f_loop, number=90000000)
    t2 = timeit.timeit(setup=f_comprehension, number=90000000)
    if t1 < t2:
        print('it is better to use a loop')
        print(str(t1) + ' vs ' + str(t2))
    else:
        print('it is better to use a list comprehension')
        print(str(t2) + ' vs ' + str(t1))

if __name__ == '__main__':
    benchmark()