import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='train',port=3306)
    cur = conn.cursor()
    #cur.execute("insert into host_list values('server','10.0.0.3','windows')")
    cur.execute('select * from host_list')
    list =  cur.fetchall()
    print list
    for line in list:
        print line,
    #conn.commit()
    cur.close()
    conn.close()


except MySQLdb.Error,e:
    print "Mysql Error%d:%s"%(e.args[0],e.args[1])
