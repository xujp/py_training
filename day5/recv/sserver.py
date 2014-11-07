#!/usr/bin/evn python

import socket 
import commands

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()

print 'Connected by',addr

while 1:
    data = conn.recv(1024)
    print "Client:%s" % data
    if not data: break 
    #user_input = raw_input("Server:==>").strip()
    #if len(user_input) == 0 : continue
    status,output = commands.getstatusoutput(data)
    conn.sendall(output)
conn.close()
