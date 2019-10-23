import socket

HOST = '127.0.0.1'
PORT = 9500
HOST_CA = '127.0.0.1'
PORT_CA = 9502
confirmation = 'Session key valid'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

request = input('Type message to server: ')

s.connect((HOST, PORT))

result = s.recv(1024).decode()
print(result)
s.close()

def checkServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST_CA, PORT_CA))
    test = 'Checking with CA: ' + serverName
    print(test)
    s.send(test.encode())
    result = s.recv(1024).decode()
    s.close()

def encrypt(message, publicKey):
    e = ''
    for char in message:
        e += chr(ord(char) + publicKey)
    return e

def main():
    PK = 0
    confirm = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    print('Connecting...')

    s.send('Hello'.encode())
    reply = s.recv(1024).decode()
    print('Server message: ' + reply)

    print('Verifying Server')
    PK = checkServer(reply)

    if (PK == None):
        print('Goodbye')
        s.send('Goodbye'.encode())
        reply = s.recv(1024).decode()
    else:
        s.send(encrypt(confirmation, PK).encode())
        reply = s.recv(1024).decode()
        print('Server message: ' + reply)
        if (reply == encrypt(confirmation + PK)):
            confirm = True
    
    while confirm:
        request = input('Type message to server (Hello does something unique, but Goodbye shuts it down): ')
        if (data == 'goodbye' or data == 'Goodbye'):
            s.send('Goodbye').encode()
            #x.send(response)
            break
        else:
            s.send(encrypt(request, PK).encode())
            reply = s.recv(1024).decode()
            if reply == encrypt('...', PK):
                print('...')
            else:
                print('Server message: ' + reply)

main()