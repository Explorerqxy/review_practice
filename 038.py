def NumberOf1Between1AndN(n):
    if n <= 0:
        return 0
    strN = str(n)
    return NumberOf1(strN)

def NumberOf1(strN):
    if not strN or strN[0] < '0' or strN > '9':
        return 0
    first = ord(strN[0]) - ord('0')
    length = len(strN)
    if length == 1 and first == 0:
        return 0
    if length ==1 and first > 0:
        return 1
    #假设strN是“12345”， numFirstDigit是数字10000~19999的第一位中的数目
    numFirstDigit = 0
    if first > 1:
        numFirstDigit = PowerBase10(length - 1)
    elif first == 1:
        numFirstDigit = ord(strN[1]) + 1
    #numOtherDigits是1346~21345除第一位之外的数位中的数目
    numOtherDigits = first * (length-1)*PowerBase10(length-2)
    #numRecursive是1~1345中的数目
    numRecursive = NumberOf1(strN[1:])

    return numFirstDigit + numOtherDigits + numRecursive

def PowerBase10(n):
    result = 0
    for i in range(10):
        result *= 10
    return result


if __name__ == '__main__':
    n = 1234
    t = NumberOf1Between1AndN(n)
    print(t)