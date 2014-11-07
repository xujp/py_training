#!/usr/bin/env python
import sys
from prettytable import PrettyTable

dict={}
with open("contacts.txt") as f:
    for i in f.readlines():
	line=i.strip().split()	
#        print line,
	dict[line[0]]=line[1:]

print dict.keys() 

while True:
        search=raw_input("Search Info:").strip()
	if(len(search)==0): continue
	if(dict.has_key(search)):
		#print  search,  '\t'.join(dict[search])
		d=dict[search]
                l = PrettyTable(["Name","Phone","Company","Email"])
        	l.align["Name"]="l"
        	l.padding_width=2		
		l.add_row([search,d[0],d[1],d[2]])
		print l
	#start fuzzy query
	else:
		count_info=0
		if(len(search)<3):
			print 'Not valid infomation,at least three words'
			continue
	        l = PrettyTable(["Name","Phone","Company","Email"])
                l.align["Name"]="l"
                l.padding_width=2
		for name,value in dict.items():
			if(name.count(search) != 0 ): 
				e = name.find(search)
				#name[:e]+'\033[32m%s\033[0m'%search+name[e+len(search):], '\t'.join(value)
				name=name[:e]+'\033[32m%s\033[0m'%search+name[e+len(search):]
				l.add_row([name,value[0],value[1],value[2]])
				count_info+=1
				continue
				
			for i in value:
				if(i.count(search)!=0 or i[1]==search):
					l.add_row([name,value[0],value[1],value[2]])
					count_info+=1
					break
		print l
		if count_info==0:
			print "Not valid record!!"
		else :
			print "Found %s records!" %count_info 
	if search=='exit':
		sys.exit()
