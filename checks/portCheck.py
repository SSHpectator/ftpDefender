import socket

FTP_PORT = 21

"""
checkPort try to connect to the ftp0s port (21),
if it can estabilish a connection then it 
returns true,
otherwise false
"""
def checkPort(host):
    s = socket.socket()
    try:
        s.connect((host, FTP_PORT))
        return True
    except:
        return False