import random


def add(x, y):
    return x + y


def ran(num):
    random_list = []
    for i in range(0, num):
        random_list.append(int(random.random() * 100))
    return random_list


def sort(list_to_be_sort):
    result = []
    length = len(list_to_be_sort)
    for i in range(0, length):
        index = 0
        max_num = list_to_be_sort[index]
        for j in range(0, len(list_to_be_sort)):
            if list_to_be_sort[j] > max_num:
                max_num = list_to_be_sort[j]
                index = j
        list_to_be_sort.pop(index)
        result.append(max_num)
    return result


list1 = ran(100)
print(list1)
list2 = sort(list1)
print(list2)
