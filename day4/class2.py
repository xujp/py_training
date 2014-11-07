import time
import tab

checkIn_list = []

class school : 
    school_name = "The old boy trainnig "
    address = "shahe distict , beijing china"
    phone = "010-8888888"
    teacher = ["alex","jack"]

class student(school):
    def __init__(self,name):
        self.name = name
    
    def checkIn(self,c): # c is current time
        if c <= 930:
            print "\033[42;1m%s\033[0m checked in..." %self.name
            time.sleep(1)
            return self.name    
        else :
            print "\033[41;1m%s is late\033[0m" % self.name
            
    def payTuition(self):
        print "%s paied tuition,the student id will be created soon"%self.name
    
s1 = student("WeiMaohai")
s2 = student("QianLiangjia")
s3 = student("JiangYiqun")


print "start to check in ..."
c_time = 929
for s in s1,s2,s3:
    checkin = s.checkIn(c_time)
    print  s.school_name,s.phone
    if checkin  is not None:
        checkIn_list.append(checkin)
        c_time += 1
    print s.address    
    
print checkIn_list
