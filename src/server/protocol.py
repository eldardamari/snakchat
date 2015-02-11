colors = { "pink"  : '\033[95m',
    "white"  : '\033[97m',
    "blue"  : '\033[94m',
    "green" : '\033[92m',
    "yellow": '\033[93m',
    "red"   : '\033[91m',
    "sky"   : '\033[96m'
    }

class Protocol (object):
    
    def __init__(self,oper):
        self.oper = oper

    def process_message(self,msg,client):
        splited = self.split_msg(msg)

        if not self.is_command(splited[0]):
            self.oper.get_room().send_all(client.get_username(),msg)
        else:
            response = self.get_command_results(splited,client)
            self.oper.get_room().send_private_msg(client.get_username(),response)

    def split_msg(self,msg):
        return msg.split(" ",1)

    def is_command(self,cmd):
        commands = ["HELP","MEMBERS","COLOR","BEEP","PRIVATE"]
        return cmd in commands 

    def get_command_results(self,splited,client):
        cmd = splited[0]
        global colors

        if cmd == "HELP":
            return self.color_system_msg(""" ** Menu - Options **
            - COLOR <color> - Changing text color, colors: {colors}
            - MEMBERS       - Prints all active users.
            - BEEP <status> - Activate beep sound for incoming messages, status: ON / OFF
            - PRIVATE <username> <msg> - Send private messages to other users.""".format(colors=colors.keys()))

        elif cmd == "MEMBERS":
           return "Active Users: "+"/".join(self.oper.get_usernames())

        elif cmd == "COLOR":
            if len(splited) == 2:
                if splited[1] in colors:
                    self.oper.set_client_color(client,colors[splited[1]])
                    return self.color_system_msg("** Color changed succssefully to {color} **".format(color=splited[1]))
            return self.color_system_msg("** Error changing your color, please choose between {colors} **".format(colors=colors.keys()))

        elif cmd == "BEEP":
            if len(splited) == 2:
                if splited[1] in ["ON","OFF"]:
                    self.oper.set_client_beep(client,splited[1])
                    return self.color_system_msg("** Changed succssefully to {status} **".format(status=splited[1]))
            return self.color_system_msg("** Error changing your color, please choose between {options} **".format(options=["ON","OFF"]))

        elif cmd == "PRIVATE":
            args = self.split_msg(splited[1])
            if len(args) >= 2:
                client_to_send = self.oper.get_room().get_client(args[0])
                if client_to_send != None:
                    client_to_send.send_msg(client.put_color("<"+client.get_username()+"> ") + self.color_system_msg("<*Private*> ") + client.put_color("".join(args[1:])))
                else:
                    return self.color_system_msg("** Error sending private message to <{username}>, user is not exist".format(username=splited[1]))
            else:
                return self.color_system_msg("** Error sending private message to <{username}>, user is not exist")

    def color_system_msg(self,msg):
        return colors["sky"] + msg + "\033[0m"
