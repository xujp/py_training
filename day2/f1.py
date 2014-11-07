import time
import fileinput

for line in fileinput.input('f_test.txt',inplace=1):
    line = line.replace("the 5 loop","change me")
    print line,



'''
f = file("f_test.txt","a")

for i  in range(0,30):
	time.sleep(1)
	f.write('the %s loop\n'% i)
	f.flush()

f.close()
'''
