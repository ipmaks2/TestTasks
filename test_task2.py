'''
Cmd to run tests:
    pytest -v -s test_task2.py
'''
from task2v2 import foo
import pytest

def setup_function():
    '''
    Prepare environment before test
    Enshure environment is OK
    '''
    pass

def teardown_function():
    '''
    Clean environment after test.
    Clear attribute with stored call names
    from completed test,
    '''
    pass

@pytest.mark.tc001
def test_as_expected_from_task(capsys):
    '''
    When called sequence as in Task #2 from mail,
    Should be expected prints as from test task.
    '''
    b = foo()
    c = foo()
    b = b()
    c = c()
    c = c()
    out, err = capsys.readouterr()
    assert out == '1\n1\n2\n2\n3\n'
    assert err == ''

@pytest.mark.tc002
def test_no_increment_with_original_name(capsys):
    '''
    When called with original name,
    Should print 1
    '''
    f = foo()
    f = foo()
    f = foo()
    f = foo()
    out, err = capsys.readouterr()
    assert out == '1\n1\n1\n1\n'
    assert err == ''

@pytest.mark.tc003
def test_no_increment_with_secondary_name(capsys):
    '''
    When called with secondary name several time,
    Should print 2
    '''
    a = foo()
    b = a()
    b = a()
    b = a()
    out, err = capsys.readouterr()
    assert out == '1\n2\n2\n2\n'
    assert err == ''

@pytest.mark.tc004
def test_increment_with_reassign_same_name(capsys):
    '''
    When called with reassigned same name,
    Should print with increment.
    '''
    f = foo()
    f = f()
    f = f()
    f = f()
    out, err = capsys.readouterr()
    assert out == '1\n2\n3\n4\n'
    assert err == ''

@pytest.mark.tc005
def test_increment_with_reassign_different_names(capsys):
    '''
    When called with reassigned different names,
    Should print with increment.
    '''
    a = foo()
    b = a()
    c = b()
    d = c()
    out, err = capsys.readouterr()
    assert out == '1\n2\n3\n4\n'
    assert err == ''


def test_original_after_secondary_name(capsys):
    '''
    When called with original name after reassigned,
    Should print 1 again after increment.
    '''
    f = foo()
    f = f()
    f = f()
    f = f()
    f = foo()
    out, err = capsys.readouterr()
    assert out == '1\n2\n3\n4\n1\n'
    assert err == ''

