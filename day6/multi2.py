import tab
from multiprocessing import Process,Manager

""" not communication among multiprocess if not use Manager module"""
name_list = []
def sayHi(name,n):
    print "hello,my name is %s, how are you?"%name,n
    name_list.append(n)
    print type(name_list),name_list


if __name__ == "__main__":
    for i in range(10):
        p = Process(target = sayHi, args = ('alex',i))
        #enable multiprocessing
        p.start()
        #next process start to performance until last process end with join function 
        p.join()

print "---------->",name_list

