import socket
s = socket.socket()  # 创建一个socket实例
host = socket.gethostname()  # 设置地址名
print(host)
port = 1234  # 设置端口号 不能低于1024
s.bind((host, port))  # 为此socket实例关联一个地址和端口号
s.listen(5)  # 设置监听队列最多5个

while True:
    print('into loop')
    client, address = s.accept()  # 开始接受客户端连接,此方法将阻塞进程,直到收到连接请求
    print('an user has connected, the address is:', address)
    client.send('you have connected'.encode())  # 发送消息,必须为byte字节类型,str类型需要进行转换
    client.close()  # 关闭连接
