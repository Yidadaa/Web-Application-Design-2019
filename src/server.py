import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print('{} wrote:'.format(self.client_address[0]))
        print(self.data)

        resp = 'HTTP/1.1 301 Moved Permanently\nLocation:http://127.0.0.1:9990'

        self.request.sendall(bytes(resp, 'utf-8'))

if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9994
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
