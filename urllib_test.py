from urllib.request import *
from socketserver import TCPServer, StreamRequestHandler

web_page = urlopen('http://www.python.org')


class Handler(StreamRequestHandler):  # 定义一个处理器类继承Stream处理器
    def handle(self):  # 重写Handel方法供服务器调用
        address = self.request.getpeername()
        print('a client has connected, the address is:', address)
        self.wfile.write('you have connected'.encode())  # 处理的是流,使用wfile属性进行通信


server = TCPServer(('', 1234), Handler)  # 创建一个TCP服务器 将自定的处理器类提供给它调用
server.serve_forever()  # 开始运行服务器




