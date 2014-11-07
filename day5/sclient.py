import socket

HOST = '192.168.93.130'
PORT = 50007

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))


while 1:
    user_input = raw_input("Client:=>>").strip()
    if len(user_input) == 0:continue
    s.sendall(user_input)
    data = s.recv(1024)
    print 'Server:=>>',data

    
s.close()
