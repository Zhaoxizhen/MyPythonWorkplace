import fileinput                                   # 1
                                                   # 2
for line in fileinput.input(inplace=True):         # 3
    line = line.rstrip()                           # 4
    num = fileinput.lineno()                       # 5
    print('{:<50} #{:2d}'.format(line, num))       # 6 左对齐的50个字符用line填充 2d使用2位十进制数num填充


