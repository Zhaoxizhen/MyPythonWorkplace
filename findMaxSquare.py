import math

maxRange = int(input("Enter a range number\n"))
list1 = list(reversed(range(maxRange)))
for num in list1:
    if num * num <= maxRange:
        print("the max number in {maxRange} is {num}".format(maxRange=maxRange, num=num))
        print("the max square in {maxRange} is {num}".format(maxRange=maxRange, num=num*num))
        break
