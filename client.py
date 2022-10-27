import socket, time

while True:
    try:
        host = socket.gethostname()
        port = 8000  # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        data = s.recv(1024)
        s.close()
        print('Received', repr(data))
    except:
        print("couldnt connect to peer")
        time.sleep(2)