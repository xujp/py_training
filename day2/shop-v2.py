#!/usr/bin/env python

product=['iphone5s','bike','car','book']
price =[5000,800,50000,300]

shop_list=[]

salary =int(raw_input("Salary:=>>"))
while True:

    print 'Product Info:'
    for i,v in zip(product,price):
        print i,v

    print "Do you want to buy some product?"
    option = raw_input("option:=>>")
    if option in product :
        option_price = price[product.index(option)]
        if salary >= option_price:
            print 'add \033[32;1m%s\033[0m to shop_list'% option
            salary-=option_price
            print 'Your balance is \033[33;1m%s\033[0m '%salary
        else:
            print "you can't afford to the product"
            if salary < min(price):       
                print "you too poor, push off"
                break
