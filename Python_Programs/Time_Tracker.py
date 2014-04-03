# This program is a timer to see how long a program takes to finish executing.
import time

def main():
    start = time.time()
    # Insert code here
    elapsed = time.time() - start
    print 'elapsed time: %3f ms' % int(round(elapsed* 1000))
main()
