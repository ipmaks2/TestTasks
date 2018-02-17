import inspect
import sys
import traceback


def foo():
    print inspect.stack()[1][4]
    return foo

foo.count = 1

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

