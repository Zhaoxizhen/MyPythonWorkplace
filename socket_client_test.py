import socket
s = socket.socket()  # 创建一个socket实例
host = 'CP-20191111JLZU'  # 设置地址
port = 1234  # 设置端口号

s.connect((host, port))  # 开始连接
msg = s.recv(1024)  # 接收消息,消息长度默认1024
print(msg)
