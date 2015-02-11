import threading, socket, select

from oper import Oper
from client import Client


CLIENTS_LIMIT = 10
RECV_BUFFER = 4096

class ThreadPerClientThread (threading.Thread):

    def __init__(self,port):
        threading.Thread.__init__(self)
        self.port = port
        self.host = 'localhost'
        self.oper = Oper()

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(10)

        print "Snakchat Server is Listening..."

        while True:
            rlist, wlist, xlist = select.select([server_socket],[],[],0)

            if rlist:
                    socket_fd, addr = server_socket.accept()
                    username = socket_fd.recv(RECV_BUFFER)

                    if self.oper.num_of_clients() < CLIENTS_LIMIT:
                        
                        new_client = Client(server_socket,\
                                            socket_fd,   \
                                            self.oper,   \
                                            username)
                        # add new user to active users
                        self.oper.add_client(new_client)
                        #start user thread
                        new_client.start()

                        print "Client <{name}> is connected".format(name=username)
                    else:
                        socket_fd.send("Error - Snakchat room is full")
                        socket_fd.close()
