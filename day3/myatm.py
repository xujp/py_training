#!/usr/bin/env python
import tab,getpass,sys
from prettytable import PrettyTable

account_file = 'account.txt'
lock_file = 'lock.txt'

#put account information in dict_account
with file(account_file) as f:
    account_list = f.readlines()
    

def login():
    while True:
        username = raw_input("Username:=>>").strip()
        if len(username) == 0 : continue
        count = 3
        for line in account_list :
            line = line.split()
            if line[0] == username :
                for i in range(3):
                    password = getpass.getpass("Password:==>")
                    if line[1] == password :
                        print 'welcome to my website'
                        break
                    else:
                        count -= 1
                        if count == 0 :
                            print "3 times logined failed ,your account is locked!"
                            sys.exit()
                        elif count == 1:
                            print "now you left %s times login chance" %count
                            continue
                        print "now you left %s times login chance" %count
                        continue
                         
login()
