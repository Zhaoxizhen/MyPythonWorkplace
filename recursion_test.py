def add(arr):
    if len(arr) == 1:  # 基线条件
        return arr[0]
    else:  # 递归条件
        return arr[0] + add(arr[1:len(arr)])


arr1 = range(6)
print(add(arr1))


def count(arr):
    if arr:  # 递归条件
        return 1 + count(arr[1:])
    else:  # 基线条件
        return 0


arr2 = range(100)
print(count(arr2))


def find_max_num(arr):
    if len(arr) == 1:  # 基线条件
        return arr[0]
    if arr[0] > find_max_num(arr[1:]):  # 递归条件
        return arr[0]
    else:  # 递归条件
        return find_max_num(arr[1:])


arr3 = [10, 50, 25, 15]
print(find_max_num(arr3))


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    elif len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    else:
        base = arr[0]
        arr_s = []
        arr_e = []
        arr_l = []
        for s in arr:
            if s < base:
                arr_s.append(s)
            elif s == base:
                arr_e.append(s)
            else:
                arr_l.append(s)
        return quick_sort(arr_s) + arr_e + quick_sort(arr_l)


arr4 = range(100)
arr4 = list(reversed(arr4))
print(arr4)
print(quick_sort(arr4))
