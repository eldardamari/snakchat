import threading, socket, select

RECV_BUFFER = 4096

class Client (threading.Thread):

    def __init__(self,  server_socket,\
                        socket_fd,\
                        oper,\
                        username):
        print username, " created"
        threading.Thread.__init__(self)
        self.server_socket = server_socket
        self.socket_fd = socket_fd
        self.oper = oper
        self.username = username

    def run(self):
        print self.username, " is active"
        while True:
            rlist, wlist, xlist = select.select([self.socket_fd],[],[],0)

            if rlist:
                # lets firsts send every message
                msg = self.socket_fd.recv(RECV_BUFFER)
                self.oper.get_room().send_all(self.username,msg)

    def get_username(self):
        return self.username

    def send_msg(self,username,msg):
        message = "<{name}>: {say}".format(name=username, say=msg)
        self.socket_fd.send(message)
