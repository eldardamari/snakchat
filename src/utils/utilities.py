CLIENTS_LIMIT = 10
RECV_BUFFER = 4096

colors = { "pink"  : '\033[95m',
    "white"  : '\033[97m',
    "blue"  : '\033[94m',
    "green" : '\033[92m',
    "yellow": '\033[93m',
    "red"   : '\033[91m',
    "sky"   : '\033[96m'
    }

user_color = "white"
ENDC = "\033[0m"
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def color_system_msg(msg):
    return colors["sky"] + msg + ENDC

def color_warning_msg(msg):
    return colors["red"] + msg + ENDC

def color_sucess_msg(msg):
    return colors["green"] + msg + ENDC

def bold_underline_text(msg):
    return BOLD + UNDERLINE + msg + ENDC
