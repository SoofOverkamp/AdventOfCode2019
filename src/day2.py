# _data = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
# _data = [1,1,1,4,99,5,6,0,99]
_data = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 5, 19, 23, 2, 9, 23, 27, 1, 27, 5, 31, 2, 31,
         13, 35, 1, 35, 9, 39, 1, 39, 10, 43, 2, 43, 9, 47, 1, 47, 5, 51, 2, 13, 51, 55, 1, 9, 55, 59, 1, 5, 59, 63, 2,
         6, 63, 67, 1, 5, 67, 71, 1, 6, 71, 75, 2, 9, 75, 79, 1, 79, 13, 83, 1, 83, 13, 87, 1, 87, 5, 91, 1, 6, 91, 95,
         2, 95, 13, 99, 2, 13, 99, 103, 1, 5, 103, 107, 1, 107, 10, 111, 1, 111, 13, 115, 1, 10, 115, 119, 1, 9, 119,
         123, 2, 6, 123, 127, 1, 5, 127, 131, 2, 6, 131, 135, 1, 135, 2, 139, 1, 139, 9, 0, 99, 2, 14, 0, 0]


def tick(data, i=0):
    op = data[i]
    if op == 99:
        return -1
    if op == 1:
        data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
    elif op == 2:
        data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
    return i + 4


def run(data):
    pc = 0
    while pc >= 0:
        pc = tick(data, pc)


for noun in range(100):
    for verb in range(100):
        data = _data[:]
        data[1] = noun
        data[2] = verb
        run(data)
        if data[0] == 19690720:
            print(100 * noun + verb)
