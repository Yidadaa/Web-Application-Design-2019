'''
用来测试socket服务器是否工作正常
'''

import socket
import sys

if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9000
    data = 'test data'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + '\n', 'utf-8'))
        received = str(sock.recv(1024), 'utf-8')
    finally:
        sock.close()

    print('Sent: {}'.format(data))
    print('Received: {}'.format(received))