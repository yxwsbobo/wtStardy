import socket

sAddress = ("127.0.0.1",8090)

'''

sServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sServer.bind(sAddress)
sServer.listen(5)

sClient, cAddr = sServer.accept()

while True:
    cData = sClient.recv(1024)
    sClient.send("Server send :%s" %(cData))


'''

sClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cAddress = ("127.0.0.1",8091)
sClient.bind(cAddress)
sClient.connect(sAddress)

while True:
    sendData = raw_input("> ")
    sClient.send("Some Info")
    sData = sClient.recv(1024)

print(sData)

