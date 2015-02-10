import threading

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

    def get_username(self):
        return self.username
