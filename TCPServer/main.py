from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
connectionSocket, add = serverSocket.accept()
print("The Server now is connected to: " + str(add))
while True:
    print("Client Message is received.")
    sentence = connectionSocket.recv(1024).decode()
    if not sentence:
        break
    length = len(sentence)
    print("The length of the client message =", length)
    connectionSocket.send(str(length).encode())
connectionSocket.close()
