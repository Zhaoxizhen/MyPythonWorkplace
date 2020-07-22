import random
import select_sort


def ran(num):
    random_list = []
    for i in range(0, num):
        random_list.append(int(random.random() * 100))
    return random_list


def search(list_to_search, target, left, right):
    middle = (left + right) // 2
    middle_num = list_to_search[middle]
    if left == right:
        return None
    if target == middle_num:  # 基线条件
        return middle
    elif target > middle_num:  # 递归条件
        return search(list_to_search, target, middle + 1, right)
    elif target < middle_num:  # 递归条件
        return search(list_to_search, target, left, middle)


list1 = ran(100)
sorted_list = select_sort.sort(list1)
sorted_list.reverse()
result = search(sorted_list, 78, 0, len(sorted_list)-1)
print(result)
