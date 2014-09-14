#!/usr/bin/env python

account = "account.txt"
lock = "lock.txt"
	
f = file(account)
name_list = f.readlines()
f.close()

while True :
	loginSuccess = False
	name = raw_input("Please enter your name:")
	name=name.strip()
	if len(name)==0: continue
	lock_list=[]
	lock_file = file(lock)
	for lock_name in lock_file.readlines():
        	lock_name = lock_name.strip('\n')
        	lock_list.append(lock_name)
	lock_file.close()
	if name in lock_list :  
		print 'Your account has been locked , please enter new account!!'
		continue
	for line in name_list:
		line=line.split()
		if line[0]==name:
			for i in range(3):
				password = raw_input("Please enter your password:")
				if password == line[1]:
					print "Welcome to my website %s @@"% name
					loginSuccess = True
					break
			else:
			    print 'you have entered three times wrong password!%s was locked'% name
			    f = file ('lock.txt','a')
			    f.write("%s\n"%name)
			    f.close()
		if loginSuccess == True : break    #jump out the top for loop 	
	if loginSuccess == True : break 	#Jump out of the while loop
