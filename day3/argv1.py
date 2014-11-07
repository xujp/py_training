#!/usr/bin/env python

import sys
print '''
     Usage:
        python argv1.py helloworld
'''
print 'The command line arguments are:'


# this is a list
print sys.argv

print sys.argv[0],'\n'
print sys.argv[1],'\n'

for i in sys.argv:
    print  i

print '\n\n The PythonPath is ',sys.path,'\n'
