#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import getpass
servername = input("mouseSMTP Server IP :")
sock = socket.socket()
sock.connect((servername, 703))
print("Welcome! What's you want to do?")
while True:
    print("1. Read mail")
    print("2. Send mail")
    print("3. Exit")
    command = input("#")
    if command == None:
        null = 1
    else:
        if command == "1":
            username = input("Login:")
            password = getpass.getpass()
            sock.send(bytes(f'exec data {username} {password} 56072020', encoding="utf8"))
            data = sock.recv(1024)
            data = data.decode('utf8')
            data = data.replace('%', ' ')
            print(data)
        else:
            if command == "2":
                send_to = input("Send To :")
                title = input("Title:")
                text = input("Text:")
                title.replace(' ', '%')
                text.replace(' ', '%')
                if send_to != None:
                    if title != None:
                        if text != None:
                            print("Message was send. Server processing your message")
                            username = input("Login:")
                            password = getpass.getpass()
                            sock.send(bytes(f'exec data {username} {password} 6702021 {send_to} {title} ;;; {text}', encoding="utf8"))
                            data = sock.recv(1024)
                            data = data.decode('utf8')
                            if data == "250":
                                print("Message successfully processed by server.")   
                            else:
                                if data == "554":
                                    print("Message failed. Check all data!")          
                        else:
                            print("Text not found.. Minimal text contents - 1 symbol")
                    else:
                        print("Title not found.. Minimal Title contents - 1 symbol")
                else:
                    print("You want send message to none? None already here and you can say it here without this SMTP Server.")
    
