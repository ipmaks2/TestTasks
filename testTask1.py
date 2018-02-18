'''
Cmd to run tests:
     pytest -v -s testTask1.py

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

def setup_function(f):
    '''
    Setup for every test. Creates new object to test.
    '''
    f.finder = PairFinder()

def teardown_function(f):
    '''
    Teardown for every test. Destroys object after testing.
    '''
    del(f.finder)

def test_emptyList():
    '''
    Test verifies: when we pass empty list, we should
    receive empty list of pairs
    '''
    f = test_emptyList.finder
    f.assignSeq([])
    assert [] == f.findPairs()
    assert '' == str(f)

def test_notNumericElement():
    '''
    Test verifies: when we pass incorrect element in list,
    we should receive error message and empty list.
    '''
    f = test_notNumericElement.finder
    f.assignSeq([2, 8, None])
    pairs = f.findPairs()
    assert 0 == len(pairs)
    assert 'error' in str(f).lower()

def test_noPairs():
    '''
    Test verifies: when we pass list with elements,
    but no pairs (with sum 10), we should receive
    empty list of pairs.
    '''
    f = test_noPairs.finder
    f.assignSeq([1])
    assert [] == f.findPairs()
    assert '' == str(f)


def test_odd():
    '''
    Test verifies: when we pass odd number of elements,
    we should receive all expected pairs.
    '''
    f = test_odd.finder
    f.assignSeq([1, 2, 3, 5, 9, 8, 5])
    pairs = f.findPairs()
    assert 3 == len(pairs)
    assert '(1, 9),(2, 8),(5, 5)' == str(f)
    for pair in pairs:
        assert pair.getPair() in [(1, 9),(5, 5),(2, 8)]

def test_even():
    '''
    Test verifies: when we pass even number of elements,
    we should receive all expected pairs.
    '''
    f = test_even.finder
    f.assignSeq([2, 8])
    pairs = f.findPairs()
    assert 1 == len(pairs)
    assert '(2, 8)' == str(f)
    for pair in pairs:
        assert pair.getPair() in [(2, 8)]


