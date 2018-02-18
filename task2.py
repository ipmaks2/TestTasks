import inspect
import sys
import traceback
import gc

debug = False

def foo():
    if (not  hasattr(foo, 'aliases')) :
        foo.aliases = {'foo()': 1}
    line =  inspect.stack()[1][4][0]
    line = line.strip()
    # print '"{}"'.format(line)
    # print type(line)

    if '=' in line:
        newName, usedName = line.split('=')
        newName = newName.strip()
        usedName = usedName.strip()
        # print newName
        # print usedName
        # print foo.aliases
        print foo.aliases[usedName]
        foo.aliases[newName+'()'] = foo.aliases.get(usedName) + 1

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
    c()

