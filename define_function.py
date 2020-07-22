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
    if target == middle_num:
        return middle
    elif target > middle_num:
        return search(list_to_search, target, middle + 1, right)
    elif target < middle_num:
        return search(list_to_search, target, left, middle)


list1 = ran(100)
sorted_list = select_sort.sort(list1)
sorted_list.reverse()
result = search(sorted_list, 78, 0, len(sorted_list)-1)
print(result)


def greatest_common_divider(x, y):
    if x == y:
        return x
    elif x > y:
        n = y
    else:
        n = x
    while n > 0:
        if x % n == 0:
            if y % n == 0:
                return n
        n -= 1


print(greatest_common_divider(81, 27))
print(greatest_common_divider(6, 9))
print(greatest_common_divider(1680, 640))
