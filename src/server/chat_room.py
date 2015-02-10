class ChatRoom (object):

    def __init__(self,room_name):
        self.room_name = room_name
        self.clients = []


    def add_client(self,client):
        self.clients.append(client)

    def remove_client(self,client):
            for client_it in self.clients:
                if client_it.get_username() == client.get_username :
                    self.clients.remove(client_it)
                    return True
            return False



