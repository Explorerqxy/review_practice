def GetUglyNumber(index):
    if index <= 0:
        return 0
    UglyNumbers = [0 for _ in range(index)]
    UglyNumbers[0] = 1
    nextUglyIndex = 1

    Multiply2 = 0
    Multiply3 = 0
    Multiply5 = 0

    while nextUglyIndex < index:
        min = Min(UglyNumbers[Multiply2] *2, UglyNumbers[Multiply3] *3, UglyNumbers[Multiply5] * 5)
        UglyNumbers[nextUglyIndex] = min

        while UglyNumbers[Multiply2] * 2 <= UglyNumbers[nextUglyIndex]:
            Multiply2 += 1
        while UglyNumbers[Multiply3] * 3 <= UglyNumbers[nextUglyIndex]:
            Multiply3 += 1
        while UglyNumbers[Multiply5] * 5 <= UglyNumbers[nextUglyIndex]:
            Multiply5 += 1

        nextUglyIndex += 1
    ugly = UglyNumbers[-1]
    return ugly

def Min(number1, number2, number3):
    min = number1 if (number1 < number2) else number2
    min = min if (min < number3) else number3

    return min

if __name__ == '__main__':
    t = GetUglyNumber(12)
    print(t)
