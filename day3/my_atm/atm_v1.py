#!/usr/bin/env python

import tab,time,sys,getpass
from prettytable import PrettyTable

account_file = "account.txt"
lock_file = "lock.txt"
credit_log = "credit_record.log"
lock_list = []

dic_account={}

with file(account_file) as f:
    account_list = f.readlines()
    for line in account_list :
        line = line.split()
        dic_account[line[0]] = line[1:]

print dic_account

with file(lock_file) as f:
    lock_l = f.readlines()
    for line in lock_l:
        line = line.strip('\n')
        lock_list.append(line)

print lock_list
    
def loger(account,tran_date,tran_type,amount,interest):
    with file(credit_log,'a') as f:
        msg="%s %s %s %s %s\n" %(account,tran_date,tran_type,amount,interest)
        f.write(msg)

def search(user_name):
    count = 0 
    a = PrettyTable(["Account","Date","Type","Amount","Interest"])
    with file(credit_log) as f:
        n = f.readlines()
        for i in n:
            i = i.split()
            if user_name == i[0]:
                b = ' '.join(i[1:3])
                a.add_row([i[0],b,i[3],i[4],i[5]])
                count+=1
        print a
        if count == 0 :
            print "The user %s is not record"%user_name

def cash_withdrawl(user_name):
    cash = int(dic_account[username][2])
    while True:
        try:
            amount = int(raw_input("How much do you want to cash withdrawl:==>:"))
            if amount <= 0:
                print "You can not cash withdrawl o and minus,input again!"
                continue
            plus_interest = int(amount * 1.05)
            if cash >= plus_interest:
                while True:
                    judge = raw_input("Are you sure cash withdrawl %s ,and plus 5 of percent total is %s.[Y/N]" %(amount,plus_interest)).strip()
                    if judge =="Y" or judge =="y":
                        cash = cash - plus_interest
                        dic_account[username][2] = str(cash)
                        with file(account_file,'wb') as f:
                            for k,v in dic_account.items(): 
                                v = ' '.join(v)
                                f.write("%s %s\n"%(k,v))
                        cash_time = time.strftime("%Y-%m-%d %H:%M:%S")
                        cash_type = "Cash_withdrawl"
                        amount_interest = plus_interest - amount
                        loger(user_name,cash_time,cash_type,amount,amount_interest)
                        print 'Cash withdrawal %s successful, and you left %s money!' % (amount, cash)
                        break
                    elif judge == 'N' or judge == 'n':
                        print 'Do nothing, and go back last menu!'
                        break
                    else:
                        print 'Invalid choice, please type "Y/y" or "N/n" to continue'
                        continue
            else:   
                print "Sorry, you have not enough money, try again!"
                continue            
            
        except ValueError:
            print "Input a integer, not string and can not input empty!"
            quit = raw_input('Do you want to exit? [Y/N]').strip()
            if quit == 'Y' or quit == 'y':
                break
            elif quit == 'N' or quit == 'n':
                continue


def choice():
    print """Usage:
                        1 : Search.

                        2 : Shopping.

                        3 : Cash withdrawal.

                        4 : Repayment.

    Type 'exit' or 'quit' to exit!\n"""
    
    choice = raw_input("what do you want do ?==>").strip()
    if choice == '1':
        search(username)
    elif choice == '2':
        pass
    elif choice == '3':
        cash_withdrawl(username)
    elif choice =='4':
        pass
    elif choice == "exit" or choice == "quit":
        print "Exit"
        sys.exit()
    else:
        print "Type 1-4 ,try again. "

while True:
    username = raw_input("username:==>").strip()
    if len(username) == 0 : continue
    elif username in lock_list:
        print "Sorry,user %s in the blacklist"%username
        sys.exit()
    elif username == "exit" or username == "quit":
        print "Exit"
        sys.exit()
    
    if dic_account.has_key(username):
        for i in range(3):
            password = getpass.getpass("Password:==>").strip()
            if password == dic_account[username][0]:
                print "Account Information"
                a = PrettyTable(['Acount','Credit','Balance'])
                a.add_row([username[:2] + "***" + username[5:],dic_account[username][1],dic_account[username][2]])
                print a                
                choice()
    
