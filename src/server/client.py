import threading,thread,  select, socket, sys
sys.path.append("..")

import utils.utilities as Utils
from protocol import Protocol

RECV_BUFFER = 4096

class Client (threading.Thread):

    def __init__(self,  server_socket,\
                        socket_fd,\
                        oper,\
                        username):
        threading.Thread.__init__(self)
        self.server_socket = server_socket
        self.socket_fd = socket_fd
        self.oper = oper
        self.username = username
        self.protocol = Protocol(oper)
        self.text_color = Utils.colors["white"]
        self.beep = "\a"

    def run(self):
        self.oper.user_join_msg(self.username)
        try:
            while True:
                rlist, wlist, xlist = select.select([self.socket_fd],[],[],0) 
                if rlist:
                    # lets firsts send every message
                    msg = self.socket_fd.recv(RECV_BUFFER).rstrip()
                    if msg:
                        self.protocol.process_message(msg,self)
        except socket.error, e:
            print "<{username}> Disconnected - Connection error: {msg}".format(username=self.username,msg=e)
            self.oper.remove_client(self)

    def get_username(self):
        return self.username

    def send_msg(self,msg):
        try:
            self.socket_fd.send(self.beep+msg+"\n")
        except:
            self.oper.remove_client(self)
            self.socket_fd.close()


    def set_text_color(self,color):
        self.text_color = color

    def put_color(self,msg):
        return "{color_begin}{say}{color_end}".\
                    format( color_begin=self.text_color,\
                            say=msg,                    \
                            color_end="\033[0m")

    def set_beep(self, status):
        self.beep = "\a" if status else ""

    def commit_suicide(self):
        self.oper.remove_client(self)
        self.socket_fd.close()
        self.oper.user_left_msg(self.get_username())
        print "Client <name> is connected".format(name=self.username)
        thread.exit()
