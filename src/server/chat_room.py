import threading

class ChatRoom (object):

    def __init__(self,room_name):
        self.room_name = room_name
        self.clients = []
        self.lock = threading.Lock()


    def add_client(self,client):
        self.clients.append(client)

    def remove_client(self,client):
        if client in self.clients:
            self.clients.remove(client)
            return True
        return False

    def send_private_msg(self,username,msg):
        self.lock.acquire()
        self.get_client(username).send_msg(username,msg+"\n")
        self.lock.release()

    def send_all(self,username,msg):
        self.lock.acquire()

        for client_it in self.clients:         
            client_it.send_msg(username,self.color_msg(username,msg))

        self.lock.release()

    def color_msg(self,username,msg):
        client = self.get_client(username)
        if client != None:
            return client.put_color(msg)
        else:
            return msg

    def get_client(self,username):
        for client_it in self.clients:
            if client_it.get_username() == username:
                return client_it
        return None
