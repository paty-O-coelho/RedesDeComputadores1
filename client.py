# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:45:44 2019

@author: patricia_sampaio


import socket, threading, sys, select

with socket.socket() as s:
    s.connect(('', 9999))
    while True:
        io_list = [sys.stdin, s]
        ready_to_read,ready_to_write,in_error = select.select(io_list , [], [])
        for io in ready_to_read:
            if io is s: # se tivermos recebido mensagem
                resp = s.recv(1024)
                if not resp:
                    print('server shutdown')
                    sys.exit()
                print('{}'.format(resp.decode()))
            else:
                msg = sys.stdin.readline() # vamos enviar mensagem
                s.send(msg.encode())
                sys.stdout.flush()
"""


#Client
import socket
serverName = '192.168.196.1' 
serverPort = 12000 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
clientSocket.connect((serverName,serverPort)) 
sentence = input('Input lowercase sentence:') 
clientSocket.send(sentence) 
modifiedSentence = clientSocket.recv(1024) 
print ('From Server:', modifiedSentence) 
clientSocket.close()



#Server
import socket
serverPort = 12000 
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
serverSocket.bind(('',serverPort)) 
serverSocket.listen(1) 
print ('The server is ready to receive') 
while 1: 
     connectionSocket, addr = serverSocket.accept()
     sentence = connectionSocket.recv(1024)
     capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence)
connectionSocket.close()




