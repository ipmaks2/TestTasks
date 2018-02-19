'''
Implemented in Python 2.7.
Module with implemented foo(), which counts
by what reference it was called.
'''
from functools import partial

count = 1

def count_calls(func, lcount=1):
    '''
    Used as decorator
    Helps to count imaginary lenght of references to
    original called function
    '''
    def callf(func, lcount):
        '''
        Used as actualy returned function to be called
        every time called with new reference, lcount
        parameter increased and updated in global variable
        '''
        global count
        count = lcount
        func()
        return partial(callf, func, lcount+1)
    return partial(callf, func, lcount)

@count_calls
def foo():
    '''
    Prints out imaginary lenght from called reference to
    function to original name foo.

    Use global variable <count>
    '''
    print count
    return foo


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

