#!/usr/bin/env python
import tab

f = file("account.txt")
account_list=f.readlines()
f.close()
print account_list

while True :
    loginSuccess = False
    name = raw_input("name:=>>")
    if len(name) == 0:continue
    f_lock = file('lock.txt')
    lk_list=[]
    lock_list = f_lock.readlines()
    for line in lock_list:
        line = line.strip('\n')
        lk_list.append(line)
    f_lock.close()
    if name in lk_list:
        print '%s can not login'%name
        continue

    for account in account_list:
        account = account.split()
        if name == account[0]:
            for i in range(3):
                password = raw_input('password:=>>')
                if password == account[1]:
                    print 'welcome to my website'
                    loginSuccess = True
                    break
            else :
                print 'your password Error is three times,%s will be locked '% name
                fl = file('lock.txt','a')
                fl.write(name+'\n')
                fl.close()
        if loginSuccess == True : break
    if loginSuccess == True : break
        
            
