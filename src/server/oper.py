import sys
sys.path.append("..")
from chat_room import ChatRoom
import utils.utilities as Utils

class Oper (object):

    def __init__(self):
        self.clients = []
        self.channels = ChatRoom("Master")


    def add_client(self, client):
        if client:
            self.clients.append(client)
            self.channels.add_client(client)
            return True
        else:
            return False

    def remove_client(self,client):
        if client in self.clients:
            self.clients.remove(client)
            self.channels.remove_client(client)
            return True
        return False

    def num_of_clients(self):
        return len(self.clients)

    def get_clients(self):
        return self.clients 
    
    def get_usernames(self):
        names = []
        for client_it in self.clients:
            names.append(client_it.get_username())
        return names

    def get_room(self):
        return self.channels

    def set_client_color(self,client,color):
        if client in self.clients:
            client.set_text_color(color)
    
    def set_client_beep(self,client,status):
        status = True if status == "ON" else False
        if client in self.clients:
            client.set_beep(status)
    def kill_client(self,client):
        if client:
            client.commit_suicide()
    
    def user_join_msg(self,username):
        self.channels.send_all("",Utils.color_system_msg("<"+username+"> joined the room")) 

    def user_left_msg(self,username):
        self.channels.send_all("",Utils.color_system_msg("<"+username+"> left the room")) 

    def username_exists(self,username):
        for client_it in self.clients:
            if client_it.get_username() == username:
                return True
        return False
