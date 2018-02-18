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
        getpair  - return one pair as tuple of ordered
                   elements

    '''
    def __str__(self):
        return '({}, {})'.format(self.num1, self.num2)

    def __repr__(self):
        return str(self.__dict__)

    def __init__(self, n1, n2):
        self.num1 = min(n1, n2)
        self.num2 = max(n1, n2)

    def getpair(self):
        '''
        returns tuple as (n1, n2)
        '''
        return (self.num1, self.num2)


class PairFinder(object):
    '''
    Helps to find pairs of numbers.

    Class attributes:
        pairsum - stores sum of pair elements, used for
                  finding pairs

    Object attributes:
        sequence - stores received list of elements,
        pairs - list of all pairs found after request by
                findPairs method


    Methods:
        __str__   - used for output pairs as string
        __init__  - constructor, creates and initialize
        assignseq - used to pass list of elements where to
                    search for pairs
        findpairs - complete search of pairs in provided
                    previously sequence
                    returns list of objects: Pair
    '''
    pairsum = 10  # Expected sum for pair

    def __str__(self):
        if self.error:
            return 'Error'
        return ', '.join([str(pair) for pair in self.pairs])

    def __repr__(self):
        return str(self.__dict__)

    def __init__(self):
        self.sequence = []
        self.pairs = []
        self.error = False

    def assignseq(self, seq):
        '''
        Assigns list of numeric elements, where search
        for pairs
        '''
        self.sequence = seq
        self.pairs = []

    def findpairs(self):
        '''
        Method to return pairs, where sum equals to pairSum
        If we call method to return pairs for first time,
        then find pairs, otherwise just return  pairs.
        '''
        if not self.pairs:
            seq = self.sequence[:]
            while seq:
                num1 = seq.pop()
                # attempt to protect from incorect
                # element in list
                try:
                    num2 = self.pairsum - num1
                    if num2 in seq:
                        seq.pop(seq.index(num2))
                        self.pairs.append(Pair(num1, num2))
                except TypeError:
                    self.error = True
                    self.pairs = []
                    break

            self.pairs.sort(key=lambda x: x.num1)
        return self.pairs


############################################################

if __name__ == '__main__':

    pair1 = Pair(1, 2)
    pair2 = Pair(2, 4)

    print pair1
    print pair2

    print pair1.getpair()
    print pair2.getpair()

    finder = PairFinder()
    finder.assignseq([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, -100, 110, 11.5, -1.5])
    print repr(finder.findpairs())
    print finder
    print repr(finder)

