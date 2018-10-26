#!/usr/bin/env python
# coding=utf-8

import socketserver
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='myapp.log',
                    filemode='w')
logger = logging.getLogger(__file__)


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # 创建一个链接,继承于socketserver中的BaseRequestHandler类
        conn = self.request
        # 发送登录提示
        conn.sendall(b"Welcome to login...")
        logger.info("Client connect...")
        while True:
            logger.info("Waitting for recving message...")
            # 接收消息
            message = conn.recv(1024)
            # print(message.decode('utf-8'))
            logger.info(message.decode('utf-8'))
            # 收到exit就退出
            if message == "exit":
                break
            # 回复消息
            # data = input("Reply message:")
            # 发送消息
            # conn.sendall(data.encode('utf-8'))


if __name__ == "__main__":
    # 实例化
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 9999,), MyServer)
    # 调用serve_forever方法
    server.serve_forever()
