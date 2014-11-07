import tab
from multiprocessing import Process,Manager

""" communication among multiprocess with Manager module"""
def sayHi(m,name,n):
    print "hello,my name is %s, how are you?"%name,n
    m.append(n)
    print m

manager = Manager()
l = manager.list()

if __name__ == "__main__":
    for i in range(10):
        p = Process(target = sayHi, args = (l,'alex',i))
        #enable multiprocessing
        p.start()
        #next process start to performance until last process end with join function 
        p.join()

print "---------->",l

