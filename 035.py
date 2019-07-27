import importlib
m = importlib.import_module('034')
def MoreThanHalfNum(numbers, length):
    if m.CheckInvalidArray(numbers, length):
        return 0
    result = numbers[0]
    times = 1
    for i in range(1, length):
        if times == 0:
            result = numbers[i]
            times = 1
        elif numbers[i] == result:
            times += 1
        else:
            times -= 1
    if not m.CheckMoreThanHalf(numbers, length, result):
        result = 0
    return result

if __name__ == '__main__':
    a = [1,2,2,2,2,2,2,2,5,6,7,8]
    r = MoreThanHalfNum(a, 12)
    print(r)