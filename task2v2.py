'''
 Module with implemented foo(), which counts
 by what reference it was called.

 It demonstartes how inspect module can be used for it.
 Preliminary version, should be improved.
'''
from inspect import stack
from operator import methodcaller
from functools import partial

count = 1

def count_calls(func, lcount=1):
    def callf(func, lcount):
        global count
        count = lcount
        func()
        return partial(callf, func, lcount+1)
    return partial(callf, func, lcount)

@count_calls
def foo():
    '''
    Prints out imaginary lenght from called reference to function
    to original name foo.
    '''
    global count
    print count
    return foo

# foo = count_calls(foo)


if __name__ == '__main__':

    f = foo()
    f = f()
    f = f()
    f = f()
    f = f()

    b = foo()
    c = foo()
    b = b()
    c = c()
    c = c()

