from functools import reduce

x = ['Python', 'programming', 'is', 'awesome!']
print(sorted(x))
print(sorted(x, key=lambda arg: arg.lower()))
print(list(filter(lambda arg: len(arg) < 8, x)))
print(reduce(lambda val1, val2: val1 + val2, x))
