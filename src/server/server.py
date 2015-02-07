import sys, getopt

port = '8888'

def main(argv):
    """
    -h => server.py -p/--port <port>
    -p => choose port to listen
    """
    global port
    try:
        opts, args = getopt.getopt(argv,"hp:",["port="])
    except getopt.GetoptError:
        print 'server.py -p <port>'
        sys.exit(2)

    for opt, arg in opts:
       if opt == '-h':
           print 'server.py -p <port>'
           sys.exit()
       elif opt in ("-p", "--port"):
           port = arg

    print port

if __name__ == "__main__":
    main(sys.argv[1:])

    """ Run Thread Per Client Service """
        ThreadPerClientThread(port)
