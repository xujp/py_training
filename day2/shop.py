#!/usr/bin/env python
import tab

product=['iphone5s','bike','car','book']
price =[5000,800,50000,300]

salary = int(raw_input("Salary:=>>"))

shopping_list=[]

while True:
    print "Product Info:"
    for i in product:
        print i , price[product.index(i)]
    print 'Do you want to buy?'
    option = raw_input('product:=>>')
    if option in product:
        p_price = price[product.index(option)]
        if salary >= p_price:
            print "add \033[32;1m%s\033[0m into the shopping_list"% option
            shopping_list.append(option)
            salary-=p_price
            print "Your current balance is \033[31;1m%s\033[0m"%salary
            continue
        else:
            print '\033[33;1mYou can not afford to buy %s\033[0m'% option
            if salary < min(price):
                print "You are too poor ,push off"
                break 
