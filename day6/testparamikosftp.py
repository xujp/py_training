#encoding:utf-8
#!/usr/bin/env python
#使用用户名和密码传输文件

import paramiko 
import sys,os

host = 'localhost'
user = 'shawn'
password = '123.com'

s = paramiko.SSHClient()
s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

t = paramiko.Transport((host,22))
t.connect(username = user, password = password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get("/tmp/unity_support_test.1","/home/shawn/unity_support_test.2")
sftp.put('/home/shawn/tuxing.py','/tmp/xuxing2.py')

s.close()
