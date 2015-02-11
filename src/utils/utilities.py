colors = { "pink"  : '\033[95m',
    "white"  : '\033[97m',
    "blue"  : '\033[94m',
    "green" : '\033[92m',
    "yellow": '\033[93m',
    "red"   : '\033[91m',
    "sky"   : '\033[96m'
    }

user_color = "white"
    
def color_system_msg(msg):
    return colors["sky"] + msg + "\033[0m"
