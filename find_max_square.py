import math

maxRange = int(input("Enter a range number\n"))
list1 = list(reversed(range(maxRange)))
for num in list1:
    if num * num <= maxRange:
        print("the max number in {maxRange} is {num}".format(maxRange=maxRange, num=num))
        print("the max square in {maxRange} is {num}".format(maxRange=maxRange, num=num * num))
        break

for num in range(99, 80, -1):
    root = math.sqrt(num)
    if root == int(root):
        print(num)
        break
else:
    print("didn't find root")


def sayHello(name='jerry', greeting='hello'):  # 关键字参数可以指定默认值
    print('{},{}!'.format(name, greeting))
