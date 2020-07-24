class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


f1 = Fibonacci()

for i in range(10):
    print(next(f1))

while f1:
    x = next(f1)
    if x > 1000:
        print(x)
        break


def flatten(nested_list):
    for sublist in nested_list:
        for element in sublist:
            yield element


nested = [[1, 2], [3, 4], [5]]
# for num in flatten(nested):
#     print(num)

num = flatten(nested)
print(list(num))


def flatten_1(nested_list):
    try:
        for sublist in nested_list:
            for element in flatten_1(sublist):
                yield element
    except TypeError:
        yield nested_list


# nested_1 = [[[1], 2], 3, 4, [5, [6, 7]], 8]
nested_1 = [0, [1, 2], 3, [[4, 5]], [[[6], 7], 8]]
num_1 = list(flatten_1(nested_1))
print(num_1)
