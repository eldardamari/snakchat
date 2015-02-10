from chat_room import ChatRoom

class Oper (object):

    def __init__(self):
        print 'in oper'
        self.clients = []
        self.channels = ChatRoom("Master")


    def add_client(self, client):
        if client:
            self.clients.append(client)
            self.channels.add_client(client)
            return True
        else:
            return False

    def num_of_clients(self):
        return len(self.clients)

    def get_clients(self):
        return self.clients 

    def get_room(self):
        return self.channels

    def set_client_color(self,client,color):
        if client in self.clients:
            client.set_text_color(color)
