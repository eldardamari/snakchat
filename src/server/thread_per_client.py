class ThreadPerClientThread(threading.Thread):

    CLIENTS_LIMIT = 10
    RECV_BUFFER = 4096

    def __init__(self,port):
        self.port = port
        self.host = 'localhost'
        self.oper = Oper()

    def __run__(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(10)

        print "Snakchat Server is Listening..."

        while True:
            rlist, wlist, xlist = select.select([server_socket],[],[],0)

            if ready_to_read:

                    socket_fd, addr = server_socket.accept()
                    username = socket_fd.recv(RECV_BUFFER)

                    if len(self.oper.clients) < CLIENTS_LIMIT:
                        self.oper.clients.append(Client(server_socket,\
                                                    socket_fd,   \
                                                    self.oper,   \
                                                    username))
                        print "Client <%s> is connected" % username
                    else:
                        socket_fd.send("Error - Snakchat room is full")
                        socket_fd.close()
