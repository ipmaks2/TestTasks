'''
Classes to find any pairs of numbers in sequence that add
up to 10.

Example:
Sample input:
    1, 8, 2, 3, 5, 7
Sample output:
    "(2, 8), (3, 7)"

Module Pairs has classes: Pair and PairFinder

Assumptions:
    - let's output pair when minimal value goes first
    - let's sort all pairs by first (minimal) number

'''
############################################################
class Pair(object):
    '''
    Stores pair and helpers for printing them out

    Methods:
        __str__  - used for printing one pair
        __repr__ - used for debug
        __init__ - constructor, stores elements in ordered
        getPair  - return one pair as tuple of ordered
                   elements

    '''
    def __str__(self):
        return '({}, {})'.format(self.n1, self.n2)

    def __repr__(self):
        return str(self.__dict__)

    def __init__(self, n1, n2):
        self.n1 = min(n1, n2)
        self.n2 = max(n1, n2)

    def getPair(self):
        '''
        returns tuple as (n1, n2)
        '''
        return (self.n1, self.n2)


class PairFinder(object):
    '''
    Helps to find pairs of numbers.

    Class attributes:
        pairSum - stores sum of pair elements, used for
                  finding pairs

    Object attributes:
        sequence - stores received list of elements,
        pairs - list of all pairs found after request by
                findPairs method


    Methods:
        __str__   - used for output pairs as string
        __init__  - constructor, creates and initialize
        assignSeq - used to pass list of elements where to
                    search for pairs
        findPairs - complete search of pairs in provided
                    previously sequence
                    returns list of objects: Pair
    '''
    pairSum = 10  # Expected sum for pair

    def __str__(self):
        if self.error:
            return 'Error'
        return ','.join([str(pair) for pair in self.pairs])

    def __init__(self):
        self.sequence = []
        self.pairs = []
        self.error = False

    def assignSeq(self, seq):
        '''
        Assigns list of numeric elements, where search
        for pairs
        '''
        self.sequence = seq
        self.pairs = []

    def findPairs(self):
        '''
        Method to return pairs, where sum equals to pairSum
        If we call method to return pairs for first time,
        then find pairs, otherwise just return  pairs.
        '''
        if not self.pairs:
            seq = self.sequence[:]
            while (seq):
                n1 = seq.pop()
                # attempt to protect from incorect 
                # element in list
                try:
                    n2 = self.pairSum - n1
                    if (n2 in seq):
                        seq.pop(seq.index(n2))
                        self.pairs.append(Pair(n1, n2))
                except TypeError:
                    self.error = True
                    self.pairs = []
                    break

            self.pairs.sort(key=lambda x: x.n1)
        return self.pairs


############################################################

if __name__ == '__main__':

    p1 = Pair(1, 2)
    p2 = Pair(2, 4)

    print p1
    print p2

    print p1.getPair()
    print p2.getPair()

    f = PairFinder()
    f.assignSeq([1,2,3,4,5,6,7,8,9, 0, 10, -100, 110, 11.5, -1.5] )
    print repr(f.findPairs())
    print f
    print f.__dict__

