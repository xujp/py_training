#!/usr/bin/env python

import sys

def readfile(filename):
    '''Print a file to standard output.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
    f.close()
# at least two argv 
if len(sys.argv) < 2:
    print 'No action specified'
    sys.exit()

print  sys.argv[0] 

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option=='version':
        print 'version 1.2'
    elif option == 'help':
        print '''\
This program prints files to the standard output.
Any number of files can specified.
Options include:
    --version : Prints the version number
    --help    : Display this help
'''
    else:
        print 'Unknown option.'
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
