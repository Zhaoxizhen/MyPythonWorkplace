import sys


def print_queen(arr):
    for i in range(8):
        for j in range(8):
            if arr[i] == j:
                print("1 ", end='')
            else:
                print("0 ", end='')
        print('')


global arr
arr = []


def queen(x, y):
    if len(arr) == 0 and x == 0 and y >= 8:
        return
    if len(arr) >= 8:  # 基线条件:列表摆满8个 寻找下一个可能
        print('找到答案:')
        print_queen(arr)
        yield arr
        y = arr.pop()
        for i in queen(len(arr), y+1):
            yield i
    if y >= 8:  # 递归条件:无法在同一行里摆下,返回上一行
        y = arr.pop()
        for i in queen(len(arr), y+1):
            yield i
    arr.append(y)  # 置入一个位置为x行,y列的皇后
    if check_queen(arr):  # 判断是否冲突,不冲突则进入下一行第一个位置
        for i in queen(len(arr), 0):
            yield i
    else:  # 冲突则往后移一个位置
        y = arr.pop()
        for i in queen(len(arr), y+1):
            yield i


def check_queen(arr):  # 检测最后一个皇后的位置是否冲突
    index = len(arr) - 1
    if len(arr) == 1:  # 只有一个的时候返回True
        return True
    for i in range(index):
        if abs(arr[i] == arr[index]):  # 在同一列
            return False
        if abs(arr[i] - arr[index]) == abs(i - index):  # 在同一斜行
            return False
    return True


sys.setrecursionlimit(1000000)
# result1 = list(queen([], 0, 0))  # 从第一行第一列开始摆下
# print_queen(result[0])
for i1 in queen(0, 0):
    print(i1)


# result = queen(arr0, 0, 0)
# print_queen(result)

# test_arr = [0, 2]
# print(check_queen(test_arr))
