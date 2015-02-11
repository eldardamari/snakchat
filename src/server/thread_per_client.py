import threading, socket, select, sys
sys.path.append("..")
import utils.utilities as Utils

from oper import Oper
from client import Client

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
        server_socket.listen(Utils.CLIENTS_LIMIT)

        print "Snakchat Server is Listening..."

        while True:
            rlist, wlist, xlist = select.select([server_socket],[],[],0)

            if rlist:
                    socket_fd, addr = server_socket.accept()
                    username = socket_fd.recv(Utils.RECV_BUFFER)
                    if self.oper.username_exists(username):
                        socket_fd.send("Error - Username already exist!")
                        socket_fd.close()
                        continue

                    if self.oper.num_of_clients() < Utils.CLIENTS_LIMIT:
                        
                        new_client = Client(server_socket,\
                                            socket_fd,   \
                                            self.oper,   \
                                            username)
                        # add new user to active users
                        self.oper.add_client(new_client)
                        #start user thread
                        new_client.start()

                        print Utils.color_sucess_msg("Client <{name}> connected".format(name=username))
                    else:
                        socket_fd.send("Error - Snakchat room is full")
                        socket_fd.close()
