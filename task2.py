from inspect import stack
from operator import methodcaller

def foo():
    if (not hasattr(foo, 'aliases')) :
        foo.aliases = {'foo()': 1}
    # line - we read from stack original line from src to 
    #        to parse name iused to call function 
    #        and name to assign returned function
    line = stack()[1][4][0]
    line = line.strip()
    # works only for line like 'name = name()'
    # just to demonstrate concept, should be improved 
    if '=' in line:
        newName, usedName = map(methodcaller('strip'),line.split('='))
        print foo.aliases[usedName]
        foo.aliases[newName+'()'] = foo.aliases.get(usedName) + 1
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

