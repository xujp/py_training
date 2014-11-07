import SocketServer
import tab,time

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        print 'Got a connection.',self.client_address[0]
        while True:
            self.data = self.request.recv(1024).strip()
            if not self.data:
                print 'Client is disconnected',self.client_address[0]
                break
            if self.data.split()[0] == 'put':
                print 'starting to receive file',self.data.split()[1]
                f = file('recv/%s'%self.data.split()[1],'wb')
                self.request.send("ReadyReceiveFile")
                while 1:
                    data = self.request.recv(4096)
                    if data == "FileSendDone":
                        print "Transfer is Done",data
                        break
                    f.write(data)
                f.close()

            if self.data.split()[0] == 'get':
                print 'starting to send file',self.data.split()[1]
                with open("recv/%s"%self.data.split()[1]) as f:
                    self.request.send(f.read())
                    time.sleep(0.5)
                    self.request.send('FileSendDone')

if __name__ == "__main__":
    HOST, PORT = "",50007 

    # Create the server, binding to localhost on port 9999
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
server.serve_forever()

