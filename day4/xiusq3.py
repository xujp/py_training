
def deco(f):
    def pack(*args,**kwargs):
        print "Going to virify "
        f(*args,**kwargs)
        print "I am finished"
    return pack

@deco
def sayHi(name):
    print 'Hello, I am %s'%name

@deco
def sayAge(name,age):
    print "I am %s, I am %s years old"%(name,age)

sayHi("alex")
sayAge("rain",25)
