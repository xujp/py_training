import MySQLdb

try:
    list1=[]
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='train',port=3306)
    cur = conn.cursor()
    for i in range(20):
        list1.append(('hostServer%s'%i,'192.168.1.%s'%i,'Centos'))
#    print list1
    cur.executemany("insert into host_list values(%s,%s,%s)",list1)

    
    cur.execute('select * from host_list')
    cur.scroll(4,mode='relative')
    print    cur.fetchone()
    #print    cur.fetchall()
    #conn.commit()
    cur.close()
    conn.close()


except MySQLdb.Error,e:
    print "Mysql Error%d:%s"%(e.args[0],e.args[1])
