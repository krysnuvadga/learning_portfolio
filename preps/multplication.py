# Python Program to print table
# of a number given range

def table(n, r):
    for i in range (1, r + 1):

        # multiples from 1 to r (range)
        print ("%d * %d = %d" % (n, i, n * i))
