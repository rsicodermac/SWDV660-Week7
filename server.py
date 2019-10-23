import socket

HOST = '127.0.0.1'
PORT = 9500
HOST_CA = '127.0.0.1'
PORT_CA = 9502

serverName = 'cryptServer'
publicKey = +1
privateKey = -1
confirmation = 'Session key valid'

def connectServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST_CA, PORT_CA))
    s.listen()
    print ('Server connected: '+ serverName + '' + str(publicKey))
    s.close()
    
def encrypt(message):
    e = ''
    for char in message:
        e += chr(ord(char) + publicKey)
    return e

def decrypt(message):
    d = ''
    for char in message:
        d += chr(ord(char) + privateKey)
    return d

def connectSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print('Connected: '+ HOST + str(PORT))
    
    while True:
    
        x, clientAddress = s.accept()
        print('Connected: ', clientAddress)
        
        data = x.recv(1024).decode()
        if (data == 'hello' or data == 'Hello'):
            response = ('Message: "Hi"  received  from' + serverName).encode()
            printData =  serverName
            #x.send(response)
            #break
        elif data == 'Goodbye':
            response = ('Goodbye').encode()
            x.send(response)
            break
        else:
            response = ('Decrypting '+ data + '       received  from' + serverName)
            d = decrypt(data)
            e = encrypt()
            print('Decrypted message: ' + d)
            if d == confirmation:
                printData = e(confirmation)
            else:
                print('...')
                e('Request Handled')
            break
    #added to send response from above while statement printData
    x.send(printData.encode())
    x.close()

def main():
    if connectServer():
        print('Server connection established...')

        while True:
            connectSocket()
    else:
        print('Error Confirmation Failed')
        exit

main()