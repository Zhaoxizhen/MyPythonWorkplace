import sys


def print_queen(arr, num):
    global count
    print('找到第', count, '个解:', arr)
    for i in range(num):
        for j in range(num):
            if arr[i] == j:
                print("1 ", end='')
            else:
                print("0 ", end='')
        print('')


global count
count = 0
global recursion_count
recursion_count = 0


def queen(num, arr, n):
    global count
    global recursion_count
    recursion_count += 1
    if len(arr) == num:  # 基线条件:放满num个
        count += 1
        print_queen(arr, num)
        print('递归次数', recursion_count)
        # yield arr
        n = arr.pop() + 1
        if len(arr) == 1 and n >= num:
            return
        return queen(num, arr, n)
    else:
        if len(arr) == 0:
            return
        if len(arr) == 1 and n >= num:
            return
        if n >= num:  # 如果在此行都没有找到合适位置,则返回上一层,尝试下一个位置
            p = arr.pop() + 1
            return queen(num, arr, p)
        else:
            for i in range(n, num):  # 在同一行最多需要尝试num次
                if check_queen(arr, i):  # 找到不冲突的位置则尝试放下一个
                    arr.append(i)
                    return queen(num, arr, 0)  # 进入下一行 位置从0开始
            p = arr.pop() + 1  # 如果num次循环仍然没有找到合适的位置,则返回上一层,尝试下一个位置
            return queen(num, arr, p)


def check_queen(arr, y):  # 检测将要放入的皇后位置是否冲突
    index = len(arr)
    for i in range(index):  # index=0时不进入循环直接返回True
        if abs(arr[i] == y) or abs(arr[i] - y) == abs(i - index):  # 在同一列或同一斜行
            return False
    return True


sys.setrecursionlimit(100000000)
# result1 = list(queen([], 0, 0))  # 从第一行第一列开始摆下
# print_queen(result[0])
# i1 = queen(8, [], 0)
# for i1 in queen(8, [], 0):
#     print(i1)
# print(i1)
for i1 in range(8):
    queen(8, [i1], 0)
# queen(8, [], 0)


# result = queen(arr0, 0, 0)
# print_queen(result)

# test_arr = [0, 2]
# print(check_queen(test_arr))
