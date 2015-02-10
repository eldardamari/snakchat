import threading, socket, select

from protocol import Protocol

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
        self.protocol = Protocol(oper)
        self.text_color = "\033[97m"

    def run(self):
        print self.username, " is active"
        while True:
            rlist, wlist, xlist = select.select([self.socket_fd],[],[],0)

            if rlist:
                # lets firsts send every message
                msg = self.socket_fd.recv(RECV_BUFFER).rstrip()
                if msg:
                    self.protocol.process_message(msg,self)

    def get_username(self):
        return self.username

    def send_msg(self,username,msg):
        self.socket_fd.send(msg)

    def set_text_color(self,color):
        self.text_color = color

    def put_color(self,msg):
        return "{color_begin}<{name}> {say}{color_end}\n".\
                    format( name=self.username,              \
                            color_begin=self.text_color,\
                            say=msg,                    \
                            color_end="\033[0m")
