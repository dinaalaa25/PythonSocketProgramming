from socket import *
serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
print("Connection is Established . Enter ""Exit"" to terminate")
sentence = input("")
while sentence != 'Exit':
     sentence = input("Input sentence ")
     clientSocket.send(sentence.encode())
     modifiedSentence = clientSocket.recv(1024)
     print('Received From Server: ', modifiedSentence.decode())
clientSocket.close()
