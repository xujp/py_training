#!/usr/bin/env python
import tab,sys
from prettytable import PrettyTable

name_dict = {}

with file("contacts.txt") as f:
    #name_list = f.readlines()
    #print name_list
    for line in f.readlines():
        line = line.strip().split()
        #print line
        name_dict[line[0]]=line[1:]

def pr():
    l = PrettyTable(['Name','Phone','Company','Address'])
    l.align["Name"] = "l"
    l.align["Phone"] = "l"
    l.align["Company"] = "l"
    l.align["Address"] = "l"
    l.padding_width = 2
    for k,v in name_dict.items():
        l.add_row([k,v[0],v[1],v[2]])
    print l


def query():
     while True:
        search = raw_input("search:=>>").strip()
        if len(search) == 0: continue
        if name_dict.has_key(search):
            l = PrettyTable(["Name","Phone","Company","Address"])
            l.add_row([search,name_dict[search][0],name_dict[search][1],name_dict[search][2]])
            print l
        else:
            count_info=0
            if len(search) < 3 : 
                print "it's too short,at least three characters"
            l = PrettyTable(["Name","Phone","Company","Address"])
            for name, value in name_dict.items():
                if name.count(search)!=0:
                    e = name.find(search)
                    name = name[:e]+'\033[32m%s\033[0m'% search+name[e+len(search):]
                    l.add_row([name,value[0],value[1],value[2]])                    
                    count_info +=1
                    continue
                for i in value:
                   # print i 
                    if i.count(search) !=0:
                        l.add_row([name,value[0],value[1],value[2]])
                        count_info+=1
            print l
        if count_info == 0 :
            print 'Not a valid record'
        else:
            print 'Found %s records'%count_info
        if search == "exit":
            break
    
def add():
    while True:
        name = raw_input("name:=>>").strip()
        if len(name) == 0: 
            print "Not input empty"
            continue
        if name_dict.has_key(name):
            print "Sorry,%s has been in the file!"% name
        elif not name_dict.has_key(name):
            # exit for return main list
            if name == "exit":
                break
            phone = raw_input("phone:=>>").strip()
            company = raw_input('company:=>>').strip()
            email = raw_input('email:=>>').strip()
            name_dict[name] = [phone,company,email]
            with file("contacts.txt",'w') as f:
                for k,v in name_dict.items():
                    v = ' '.join(v)
                    f.write("%s %s\n"%(k,v)) 
            print "Add user %s to file success!"% name

def modify():
    while True:
        name = raw_input('name:=>>').strip()
        if len(name) == 0 : 
            print "Not input empty"
            continue
        if name_dict.has_key(name):
            phone = raw_input("phone:=>>").strip()
            company = raw_input('company:=>>').strip()
            email = raw_input('email:=>>').strip()
            name_dict[name][0]=phone
            name_dict[name][1]=company
            name_dict[name][2]=email
            with file("contacts.txt",'wb') as f:
                for k,v in name_dict.items():
                    v = ' '.join(v)
                    f.write("%s %s\n"%(k,v))
            print "modify %s success!" %name 
        elif name == "exit":
            break                   

def delete():
    while True:
        name = raw_input("name:=>>").strip()
        if len(name) == 0 : 
            print "Not input empty!"
            continue
        if name_dict.has_key(name):
            del name_dict[name]
            with file("contacts.txt","wb") as f:
                for k,v in name_dict.items():
                    v = ' '.join(v)
                    f.write('%s %s\n'%(k,v))
            print "delete user %s success!"% name
        elif name == "exit":
            break

def choice():
    while True:
        print """
                 Usage :
                    A/a : add a user
                    Q/q : search user
                    M/m : modify user
                    D/d : delete user
                    P/p : print all users
                    exit : return a mainmenu
                    quit : exit the program
"""
        option = raw_input("option:==>").strip()
        if option == "A" or option == "a":
            add()
        elif option == "Q" or option == "q":
            query()
        elif option == "M" or option == "m":
            modify()
        elif option == "D" or option == "d":
            delete()
        elif option == "P" or option == "p":
            pr()
        elif option == "quit":
            sys.exit() 
            
if __name__ == "__main__":
    choice()
