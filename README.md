# mouseSMTP
mouseSMTP Server and Client on Python. OpenSource Program.
![Screenshot](screenshot.png)
It's free and very fast Python-based Mail Server + Client emulator, works like really SMTP Server and client.

What's you can do?

SERVER PART
 - Send messages
 - Accept messages
 - View IP's working on this server
 - Control Servers
 
CLIENT PART
 - Send messages
 - Get messages
 - Delete all messages(In future)

It's minimal version, first stable release. If you found a bug, please, say about this.

If you need, you can view code of mouseSMTP Server or client and create own version, but please, you need understand about GPL License v3.0

# How to create Server?

Parts
 - Download run.py
 - If you need, you can build it with pyinstaller.
 - Create files {
 
    config.conf - Configuration file
    user.db - User file with messages.
    users.db - Encrypted data base of users, password and usernames.SHA512.
 
 }
 Write to users.db that's record:
    b14361404c078ffd549c03db443c3fede2f3e534d73f78f77301ed97d4a436a9fd9db05ee8b325c0ad36438b43fec8510c204fc1c1edb21d0941c00e9e2c1ce2:b14361404c078ffd549c03db443c3fede2f3e534d73f78f77301ed97d4a436a9fd9db05ee8b325c0ad36438b43fec8510c204fc1c1edb21d0941c00e9e2c1ce2

it's record works like
user:user

Password : user
Username : user

You need manually all required users or make a web site and make automatic creation of users on registration or another service.

in user.db you can add your messages by default
