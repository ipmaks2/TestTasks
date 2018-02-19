'''
Implemented with Python 2.7 and pytest.

Cmd to run tests:
     pytest -v -s test_task1.py

Smoke tests For PairFinder:

#1 Pass Empty List
#2 List without pairs
#3 Odd num elements
#4 Even num elements
#5 Incorrect element in list (not numeric)

Assert 1 for return pairs list
assert 2 for formatted string
Assert 3 for object count

'''

from task1 import PairFinder
import pytest

def setup_function(func):
    '''
    Setup for every test. Creates new object to test.
    '''
    func.finder = PairFinder()

def teardown_function(func):
    '''
    Teardown for every test. Destroys object after testing.
    '''
    del func.finder

@pytest.mark.tc001
def test_empty_list():
    '''
    Test verifies: when we pass empty list, we should
    receive empty list of pairs
    '''
    finder = test_empty_list.finder
    finder.assignseq([])
    assert finder.findpairs() == []
    assert str(finder) == ''

@pytest.mark.tc002
def test_not_numeric_element():
    '''
    Test verifies: when we pass incorrect element in list,
    we should receive error message and empty list.
    '''
    finder = test_not_numeric_element.finder
    finder.assignseq([2, 8, None])
    pairs = finder.findpairs()
    assert len(pairs) == 0
    assert 'error' in str(finder).lower()

@pytest.mark.tc003
def test_no_pairs():
    '''
    Test verifies: when we pass list with elements,
    but no pairs (with sum 10), we should receive
    empty list of pairs.
    '''
    finder = test_no_pairs.finder
    finder.assignseq([1])
    assert finder.findpairs() == []
    assert str(finder) == ''

@pytest.mark.tc004
def test_odd():
    '''
    Test verifies: when we pass odd number of elements,
    we should receive all expected pairs.
    '''
    finder = test_odd.finder
    finder.assignseq([1, 2, 3, 5, 9, 8, 5])
    pairs = finder.findpairs()
    assert len(pairs) == 3
    assert str(finder) == '(1, 9), (2, 8), (5, 5)'
    for pair in pairs:
        assert pair.getpair() in [(1, 9), (5, 5), (2, 8)]

@pytest.mark.tc005
def test_even():
    '''
    Test verifies: when we pass even number of elements,
    we should receive all expected pairs.
    '''
    finder = test_even.finder
    finder.assignseq([2, 8])
    pairs = finder.findpairs()
    assert len(pairs) == 1
    assert str(finder) == '(2, 8)'
    for pair in pairs:
        assert pair.getpair() in [(2, 8)]


