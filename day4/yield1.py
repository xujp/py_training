import time

'''yield can transfer a function into iter'''
def countNum():
    for i in range(10):
        print 'the %s time'%i
        yield i

a = countNum()

print a.next()
#print a.next()
#print a.next()
#print a.next()
#print a.next()

time.sleep(4)

print a.next()
