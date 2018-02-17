'''
Classes to find any pairs of numbers in sequence that add up to 10.
Example:
Sample input:
    1, 8, 2, 3, 5, 7
Sample output:
    "(8, 2), (3,7)"

Module Pairs has classes: Pair and PairFinder

Assumptions:
    - numbers should be less then 10
    - zeros not acceptable
'''
##############################################################################
class Pair(object):
    '''
    Stores pair and helpers for printing them out
    '''
    def __str__(self):
        return '({}, {})'.format(self.n1, self.n2)

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2


class PairFinder(object):
    '''
    Helps to find pairs of numbers.
    '''
    pairSum = 10  # Expected sum for pair

    def __str__(self):
        return ','.join([pair.__str__() for pair in self.pairs])

    def __init__(self):
        self.sequence = []
        self.pairs = []

    def assignSeq(self, seq):
        self.sequence = seq

    def findPairs(self):
        seq = self.sequence
        while (seq):
            n1 = seq.pop() 
            n2 = self.pairSum - n1
            if seq.count(n2):
                seq.pop(seq.index(n2))
                self.pairs.append(Pair(n1, n2))
        return self.pairs


##############################################################################
##############################################################################

if __name__ == '__main__':

    p1 = Pair(1, 2)
    p2 = Pair(2, 4)

    print p1
    print p2

    f = PairFinder()
    f.assignSeq([1,2,3,4,5,6,7,8,9] )
    f.findPairs()
    print f


