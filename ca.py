import socket

HOST = '127.0.0.1'
PORT = 9502

def CertificateAuthority():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.bind((HOST, PORT))
    c.listen()
    certificationDictionary:{}
    print('CA running on host: ' + HOST +' port: ' + str(PORT))
    
    while True:
        response = ''
        x, addr = c.accept()
        data = x.recv(1024).decode().split(',')
        a = data[0]
        b = data[1]
        
        print(a + ' ' + b )
        session.close()

CertificateAuthority()

