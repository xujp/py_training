#!/usr/bin/env python

#print 'Hello , World!'

import tab

for i in range(3):
    name = raw_input("what is your name:").strip()
    if len(name) == 0:
        continue
    break 
#the else will performance if loop is end normarly 
else:
    print 'the loop is end'
age = raw_input("what is your age:")
sex = raw_input("what is your sex:").strip()
job = raw_input("what is your job:")

print '''Person info:
    
    Name:%s
    Age :%d
    Sex :%s
    Job :%s
'''%(name,int(age),sex,job)

if int(age) <= 28 :
    print 'You can have a holiday'
elif sex == 'F':
    print "Let's think so "
else:
    print 'You must go to work'
