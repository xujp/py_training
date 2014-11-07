import tab,sys,getpass

def log(i):
    with file("variable.txt","a") as f:
        f.write("%s\n"%i)
count = 3
while True:
    for i in range(3):
        password = getpass.getpass("password:==>").strip()
        if password == "abc":
            print "Login success"
            sys.exit()
        elif len(password) == 0 :
            print "Password not empty"
        elif password =="exit":
            print "exit"
            sys.exit()
        else :
            count -= 1   
            if count == 0:
                print "3 times login fail"
            elif count == 1 :
                print "%s times left "% count
                continue
            print "%s times left "%count
            continue 
