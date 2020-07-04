#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import time
import os
import hashlib


sock = socket.socket()
sock.bind(('', 703))
sock.listen(20)
def FileSave(filename,content):
    with open(filename, "a") as myfile:
        myfile.write(content)
global users 
users = []
global quota_
quota_ = []
def server_thread(conn, addr):
    print(f"{time.ctime()} |", addr, 'Connected')
    print(f"{time.ctime()} | 250 0.0.0.0, I am glad to meet you")
    print(f"{time.ctime()} | 250 Ok")
    print(f"{time.ctime()} | QUOTA CONFIGURED")
    while True:
        try:
            data = conn.recv(1024)
        except:
            print(addr, '221 Bye')
            break
        if not data:
            print(addr, '221 Bye') 
            break 
        data = data.decode('utf8')
        args = data.split(' ')
        if args[0] == "exec":
            if args[1] == "data":
                secure_Data_login = hashlib.sha512(bytes(args[2], 'utf8')).hexdigest()
                secure_Data_pass = hashlib.sha512(bytes(args[3], 'utf8')).hexdigest()
                if args[2] != None and args[3] != None and f'{secure_Data_login.lower()}:{secure_Data_pass.lower()}' in open("users.db", 'r').read():
                    print(F"{time.ctime()} | Executing..")
                    if args[4] == "56072020":
                        print(f"{time.ctime()} | reading mail..")
                        conn.send(bytes(f"{open(f'{args[2]}.db', 'r').read()}", encoding="utf8"))
                    else:
                        if args[4] == "6702021":
                            if os.path.isfile(f"{args[5]}.db"):
                                print(f"{time.ctime()} | Server checked mail... ALL OK.")
                                send_to = args[5]
                                print(f"{time.ctime()} | 250 Ok")
                                data = ' '.join(args[6:]).split(';;;')
                                title = data[0]
                                description = ';;;'.join(data[1:])
                                print(f"{time.ctime()} | 250 Ok")
                                print(f"{time.ctime()} | REQUEST RECEIVED, SENDING MESSAGE..")
                                print(f"{time.ctime()} | REQUEST RECEIVED, ")
                                print(f"{time.ctime()} | 250 Ok")
                                FileSave(f"{args[5]}.db", f"{time.ctime()}|From:{args[2]}@{my_ip}|\nTitle:{title}\nText:{description}\n")
                                print(f"{time.ctime()} | REQUEST RECEIVED, MESSAGE WAS SEND.")
                                conn.send(b"250")
                                print(f"{time.ctime()} | 221 Bye")
                            else:
                                print(f"{time.ctime()} | Server checked mail... BAD_REQUEST.")
                                print(args)
                                print(args[4])
                        else:
                            print("WTFFFF")
                else:
                    print(F"{args[2]}:{args[3]} | Failed to exec.")
while True:
    conn, addr = sock.accept()
    thread = threading.Thread(target=server_thread, args=(conn, addr)) # Создаём поток server_thread с аргументами conn и addr
    thread.start() # Запускаем поток. Данный while True принимающий подключения всё ещё будет работать
