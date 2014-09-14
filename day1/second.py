#!/usr/bin/env python

name = raw_input('what is your name?')
age = int(raw_input('what is your age?'))
sex = raw_input('what is your sex?')
job = raw_input('what is your job?')
print """ Personal Information:
	Name:%s
	Age:%d
	Sex:%s
	job:%s
	
"""%(name,age,sex,job)

if age<=28:
	print "you can take a holiday"	
elif sex == "F":
	print "let me think ..."
else:
	print "you are too old!"

