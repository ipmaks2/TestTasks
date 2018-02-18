'''
Cmd to run tests:
    pytest -v -s test_task2.py
'''
from task2 import foo

attr2del = 'aliases'

def setup_function():
    assert hasattr(foo, attr2del) == False

def teardown_function():
    if hasattr(foo,attr2del ):
        delattr(foo, attr2del)

def test_as_expected_from_task(capsys):
    b = foo()
    c = foo()
    b = b()
    c = c()
    c = c()
    out, err =  capsys.readouterr()
    assert out == '1\n1\n2\n2\n3\n'

def test_no_increment_with_original_name(capsys):
    f = foo()
    f = foo()
    f = foo()
    f = foo()
    out, err =  capsys.readouterr()
    assert out == '1\n1\n1\n1\n'

def test_no_increment_with_secondary_name(capsys):
    a = foo()
    b = a()
    b = a()
    b = a()
    out, err =  capsys.readouterr()
    assert out == '1\n2\n2\n2\n'

def test_increment_with_reassign_same_name(capsys):
    f = foo()
    f = f()
    f = f()
    f = f()
    out, err =  capsys.readouterr()
    assert out == '1\n2\n3\n4\n'

def test_increment_with_reassign_different_names(capsys):
    a = foo()
    b = a()
    c = b()
    d = c()
    out, err =  capsys.readouterr()
    assert out == '1\n2\n3\n4\n'


