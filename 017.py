def RecorderOddEven(data, length):
    if data == None or length <= 0:
        return
    pBegin = 0
    pEnd = length - 1
    while pBegin < pEnd:
        while pBegin < pEnd and data[pBegin] & 0x1 != 0:
            pBegin += 1
        while pBegin < pEnd and data[pEnd] & 0x1 == 0:
            pEnd -= 1
        if pBegin < pEnd:
            data[pBegin], data[pEnd] = data[pEnd], data[pBegin]

if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,8,9]
    RecorderOddEven(data, 9)
    print(data)