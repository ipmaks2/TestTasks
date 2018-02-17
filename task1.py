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
    - numbers should be less then 10
    - zeros not acceptable
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
        pair = (n1, n2)
        nMin = min(pair)
        nMax = max(pair)
        self.n1 = nMin
        self.n2 = nMax

    def getPair(self):
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
        self.sequence = seq
        self.pairs = []

    def findPairs(self):
        if not self.pairs:
            seq = self.sequence[:]
            while (seq):
                n1 = seq.pop()
                try:
                    n2 = self.pairSum - n1
                    if seq.count(n2):
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
    f.assignSeq([1,2,3,4,5,6,7,8,9] )
    f.findPairs()
    print f
    print f.__dict__

