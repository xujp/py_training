#!/usr/bin/env python

'''
tx_dict={}
with open('contacts.txt') as f :
    line = f.readlines()    
    for i in line:
        i = i.strip().split() 
        tx_dict[i[0]] = i[1:]
print tx_dict
    
'''

contacts ={

	'shawn' : 18920290380,
	'rachel' : [134999999, 'student',25],
	'rain' : {'age':28}

}	


if contacts.has_key('shawn'):print '======'

print contacts
#for i in contacts:
#    print i,i.count('r')
    

#modify
#contacts['shawn']=888888888

#delete
#del contacts['rain']

#add 
contacts['alex']=77777777

for k,v in contacts.items():
	print k,v
