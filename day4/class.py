import sys

print sys.argv
class Dog:
    #self.name is  a class variable
    def __init__(self,name):
        self.name = name    

    #class funuction must be given a argument of self
    def bulk(self):
        print 'wang wang,my name is %s'%self.name
        #call a private function
        self.__auth()
    def eat(self,food_type):
        if food_type == "meat":
            print 'Thanks, master'
        else:
            print 'I do not like eat it'
    #private function
    def __auth(self):
        print 'can not be called outside of the class'

    def __del__(self):
        print 'the end'

D = Dog('jack')

D.bulk()    

D.eat('meat')
D.eat('fjf')
