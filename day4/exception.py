import tab

class myExcept(Exception):
    pass

while True:
    try:
        int(raw_input("Please input your age:"))
        a = ['alex','jack','shawn']
        #a[4]
        # manual a exception with raise
        #if "rain" not in a : raise ValueError
       # if "rain" not in a : raise myExcept
  #print  a error infomation with a variable    
    except ValueError,e :
        print "You must input a interger.\n",e
    except IndexError:
        print "Your index is too big"
    except myExcept:
        print "hahaha"
    else:
        print 'no exception you can performance me'
    #close database connction with it 
   # finally :
    #    print 'you are always performance me'
