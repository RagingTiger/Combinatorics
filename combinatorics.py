#!/usr/bin/env python

'''
Author: John D. Anderson
Email: jander43@vols.utk.edu
Usage: combinatorics -n
Program Description:
    Simple combination generating program given a size of number list.

Theory:
    If given a list [1, 2, 3], all combinations can be generated as follows:

                                    1
                                    |
                                    |
                                   / \
                                  /   \
                                 /     \
                                /       \
                              21         12
                             /            \
                            |              |
                           /|\            /|\
                          / | \          / | \
                       321 231 213    312 132 123
'''

# libraries
import sys
import math


# functions
def combinations(n):
    '''
    Function to generate combinations of all orderings of numbers in the range
    form 1 to "n".
    '''
    # convert n to int
    N = int(n)

    # gen starting list
    numbers = [str(x) for x in range(1, N + 1)]

    # calulate/print factorial
    f = math.factorial(N)
    print 'Combinations | Factorial Value: {0}'.format(f)

    # function
    def recur_combine(entry, clist, num):
        '''
        Function to recursively build all possible ordering combinations of
        elements in a list.
        '''
        # if max depth reached, print combo
        if entry == num:
            print ''.join(clist)
            return

        # build combinations recursively
        for i in range(entry + 1):
            # copy and recurse
            copy = clist[:]
            copy.insert(i, numbers[entry])
            recur_combine(entry + 1, copy, num)

    # start recursion
    recur_combine(1, [numbers[0]], N)

    # exit
    return


# executable
if __name__ == '__main__':
    if len(sys.argv) > 1:
        combinations(sys.argv[1])

    else:
        sys.exit('\nusage: combinatorics -n\n')
