#!/usr/bin/env python
# coding=utf-8
import socket
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='/tmp/myapp.log',
                    filemode='w')
logger = logging.getLogger(__file__)


sock = socket.socket()
# 连接服务端
# sock.connect(('', 9999, ))
sock.connect(('192.168.8.193', 9999, ))
login = sock.recv(1024)
logger.info(login.decode('utf-8'))
while True:
    message = input("Please input the message:").strip()
    if message == "exit":
        sock.sendall(b'exit')
        break
    else:
        sock.sendall(message.encode('utf-8'))
        print("Waitting for recving message...")
        data = sock.recv(1024)
        print(data.decode('utf-8'))
sock.close()
