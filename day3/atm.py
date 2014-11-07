#!/usr/bin/env python

import tab,sys,getpass,cPickle,time
from prettytable import PrettyTable

account_file = 'account.txt'
lock_file = 'lock.txt'
credit_log = 'credit_record.log'
lock_list = []
dic_account = {}

with open(account_file) as f:
    n = f.readlines()
    for i in n:
	i = i.split()
	dic_account[i[0]] = i[1:]

with open(lock_file) as f:
    n = f.readlines()
    for i in n:
	i = i.strip('\n')
	lock_list.append(i)

def choice():
    while True:
	print """Usage:
		    1 : Search.

		    2 : Shopping.

		    3 : Cash withdrawal.

		    4 : Repayment.

Type 'exit' or 'quit' to exit!\n"""
	choice = raw_input('What do you want to do? ==> ').strip()
	if choice == '1':
	    search(username)
	elif choice == '2':
	    shopping()
	elif choice == '3':
	    cash_withdrawal(username)
	elif choice == '4':
	    repayment(username)
	elif choice == 'quit' or choice == 'exit':
	    print 'Exit!'
	    sys.exit()
	else:
	    print 'Type 1-4 to continue, try again!'

def repayment(pay_account):
    while True:
	source_ba = int(dic_account[username][2])
	try:
	    amount = int(raw_input('Amount: ==> '))
	    if amount <= 0:
		print 'Can not repayment with 0 or minus, input again!'
		continue
	    while True:
		judge = raw_input('Are you sure repayment %s? [Y/N]' % amount).strip()
		if judge == 'Y' or judge == 'y':
		    now_ba = source_ba + amount
		    dic_account[username][2] = str(now_ba)
		    with open(account_file, 'wb') as f:
			for k, v in dic_account.items():
			    v = ' '.join(v)
			    f.write('%s %s\n' % (k, v))
		    pay_time = time.strftime("%Y-%m-%d %H:%M:%S")
		    pay_type = 'Repayment'
		    pay_interest = '0'
		    loger(username, pay_time, pay_type, amount, pay_interest)
		    print 'Repayment %s successfully, now you left %s money!' % (amount, now_ba)
		    break
		elif judge == 'N' or judge == 'n':
		    print 'Nothing to do, go back the last menu!'
		    break
		else:
		    print 'Invalid choice, please type "Y/y" or "N/n" to continue'
		    continue
	except ValueError:
	    print "Input a integer, not string and can not input empty!"
	    quit = raw_input('Do you want to exit? [Y/N]').strip()
	    if quit == 'Y' or quit == 'y':
		break
	    elif quit == 'N' or quit == 'n':
		continue	

def cash_withdrawal(user_name):
    cash = int(dic_account[username][2])
    while True:
	try:
	    amount = int(raw_input('How much do you want to cash withdrawal : ==> '))
	    if amount <= 0:
		print 'Can not cash withdrawal 0 and minus, input again!'
		continue
	    plus_interest = int(amount * 1.05)
	    if cash >= plus_interest:
		while True:
		    judge = raw_input('Are you sure cash withdrawal %s, and plus 5 of percent interest total is %s. [Y/N]' % (amount, plus_interest)).strip()
		    if judge == 'Y' or judge == 'y':
			cash = cash - plus_interest
			dic_account[username][2] = str(cash)
			with open(account_file, 'wb') as f:
			    for k, v in dic_account.items():
				v = ' '.join(v)
				f.write('%s %s\n' % (k, v))
			cash_time = time.strftime("%Y-%m-%d %H:%M:%S")
			cash_type = 'Cash_Withdrawal'
			cash_interest = plus_interest - amount
			#cash_interest = '5%'
			loger(username, cash_time, cash_type, amount, str(cash_interest))
			print 'Cash withdrawal %s successful, and you left %s money!' % (amount, cash)
			break
		    elif judge == 'N' or judge == 'n':
			print 'Do nothing, and go back last menu!'
			break
		    else:
			print 'Invalid choice, please type "Y/y" or "N/n" to continue'
			continue
	    else:
		print 'Sorry, you have not enough money, try again!'
		continue
	except ValueError:
	    print "Input a integer, not string and can not input empty!"
	    quit = raw_input('Do you want to exit? [Y/N]').strip()
	    if quit == 'Y' or quit == 'y':
		break
	    elif quit == 'N' or quit == 'n':
		continue	

def search(user_name):
    count = 0
    with open(credit_log) as f:
	n = f.readlines()
	for i in n:
	    i = i.split()
	    b = ' '.join(i[1:3])
	    if username == i[0]:
		a = PrettyTable(['Account', 'Date', 'Type', 'Amount', 'Interest'])
		a.add_row([i[0], b, i[3], i[4], i[5]])
		print a
		count += 1
	if count == 0:
	    print 'Empty record, would you want to buy something?'

def loger(account, date, credit_type, amount, interest):
    message = '%s %s %s %s %s\n' % (account, date, credit_type, amount, interest)
    with open(credit_log, 'a') as f:
	f.write(message)

def shopping():
    products_list = ['mac', 'iphone', 'ipad']
    prices_list = [1, 2, 3]
    shoplist = []

    balance = int(dic_account[username][2])
    while True:
	print 'This is a shopping list:\n'
	for l in products_list:
	    p = prices_list[products_list.index(l)]
	    print '%s\t%s' % (l, p)
	product = raw_input('Choose one what you want to buy : ==> ').strip()
	if product in products_list:
	    price = prices_list[products_list.index(product)]
	    if balance > price:
		balance -= price
		shoplist.append(product)
		dic_account[username][2] = str(balance)
		with open(account_file, 'wb') as f:
		    for k, v in dic_account.items():
			v = ' '.join(v)
			f.write('%s %s\n' % (k, v))
		shopping_time = time.strftime("%Y-%m-%d %H:%M:%S")
		shoping_type = 'B(%s)' % product
		shoping_interest = 0
		loger(username, shopping_time, shoping_type, price, shoping_interest)
		print 'You bought %s into your shopping list.' % shoplist
		print 'Now, you left %s money.' % balance
		continue
	    elif balance < min(prices_list):
		print 'Sorry, you have not enought money.'
		print 'Your shopping list is %s.' % shoplist
		print 'Now, you left %s money.' % balance
		print 'Going to exit!'
		break
	    else:
		print "Your money can not afford '%s' product, try another one!" % product
		continue
	elif product == 'quit' or product == 'exit':
	    print 'Your shopping list is %s.' % shoplist
	    print 'Now, you left %s money.' % balance
	    print 'Have nice day, goodbye!'
	    break
	else:
	    print 'Not a valid product, input again!'
	    continue

while True:
    username = raw_input('Username : ==> ').strip()
    if username in lock_list:
	print 'Sorry, user %s is already in blacklist!' % username
	sys.exit()
    elif username == 'quit' or username == 'exit':
	print 'Exit!'
	sys.exit()
    elif len(username) == 0:
	print 'Can not input empty, try again!'
	continue
    if dic_account.has_key(username):
	count = 3
	while True:
	    for n in range(3):
		password = getpass.getpass('Password : ==> ').strip()
		if password == dic_account[username][0]:
		    #print 'Welcome %s login my system!' % username
		    print 'Account information:'
		    a = PrettyTable(['Account', 'Credit', 'Balance'])
		    a.add_row([username[:2] + '***' + username[5:], dic_account[username][1], dic_account[username][2]])
		    print a
		    choice()
		elif len(password) == 0:
		    print 'Empty password, try again!'
		    break
		elif password == 'exit' or password == 'quit':
		    print 'Exit!'
		    sys.exit()
		else:
		    count -= 1
		    if count == 0:
			print '3 times to login failed, %s is locked in blacklist!' % username
			with open(lock_file, 'a') as f:
			    f.write('%s\n' % username)
			sys.exit()
		    elif count == 1:
			print 'Password is wrong, now you left %s time to login!' % count
			continue
		    print 'Password is wrong, now you left %s times to login!' % count
		    continue
    else:
	print 'Not a valid account, try again!'
	continue
