import sys, socket, select

sys.path.append("..")
import utils.utilities as Utils

user_color = "white"

def start_chat():
    if(len(sys.argv) < 4) :
        print 'Please use format: python client.py username hostname port'
        sys.exit()

    username = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
        s.send(username)
    except :
        print 'Error - Problem with connection to Snakchat server'
        sys.exit()
     
    print Utils.color_sucess_msg(Utils.bold_underline_text('** Welcome to Snakchat **'))
    print_prompt(username)
     

    while 1:
        socket_list = [sys.stdin, s]
        sys.stdout.write(Utils.colors[user_color])
         
        rlist, wlist, xlist = select.select(socket_list , [], [])
         
        for sock in rlist:
            if sock == s:
                data = sock.recv(Utils.RECV_BUFFER)
                if not data :
                    print '\nError - Snakchat disconnected you'
                    sys.exit()
                else :
                    delete_line()
                    sys.stdout.write(data)
                    print_prompt(username)
            
            else :
                msg = sys.stdin.readline()
                check_color_change(msg.rstrip())
                s.send(msg)
                print_prompt(username)

def print_prompt(username): 
    sys.stdout.write(Utils.colors[user_color]+'<'+username+'> '); sys.stdout.flush()

def delete_line():
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    print(ERASE_LINE + CURSOR_UP_ONE)

def check_color_change(msg):
    get_command_results(split_msg(msg))

def split_msg(msg):
    return msg.split(" ",1)

def get_command_results(splited):
    global user_color
    cmd = splited[0]

    if cmd == "COLOR":
        if len(splited) == 2:
            if splited[1] in Utils.colors:
                user_color = splited[1]

if __name__ == "__main__":
    sys.exit(start_chat())
