#!/usr/bin/env python
import tab

a = lambda i : i**2
print a(3)

d=lambda i,x : i**2/(x-i)
print d(2,6)

e=map(lambda i : i**2 ,[x for x in range(5)])
print e
