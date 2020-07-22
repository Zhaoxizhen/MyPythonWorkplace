def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value


s = ArithmeticSequence(1, 2)
print(s[4])
s[4] = 3
print(s[4])
print(s[5])


class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)  # python3 中的super函数应该不提供任何参数
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)


cl = CounterList(range(10))
print(cl)
cl.reverse()
print(cl)
del cl[3:6]
print(cl.counter)
print(cl[4] + cl[2])
print(cl.counter)
