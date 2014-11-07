import socket
import tab,time

HOST = '192.168.93.130'
PORT = 50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))


while 1:
    user_input = raw_input("Client:=>>").strip()
    if len(user_input) == 0:continue
    s.sendall(user_input)
    f = file(user_input.split()[1],'wb')
    while 1:
        data = s.recv(1024)
        if data == 'ReadyReceiveFile':
            with open(user_input.split()[1]) as f:
                s.sendall(f.read())
                time.sleep(0.5)
                s.sendall('FileSendDone')
            break
        if data == "FileSendDone":
            print 'Transfer is done' ,data
            break
        f.write(data)
    f.close()   
    
s.close()
