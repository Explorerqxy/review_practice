def digitAtIndex(index):
    if index < 0:
        return -1
    digits = 1
    while True:
        numbers = countOfIntegers(digits)
        if index < numbers * digits:
            return DigitAtIndex(index, digits)
        index -= digits * numbers
        digits += 1

def countOfIntegers(digits):
    if digits == 1:
        return 10
    count = 10**(digits - 1)    #python中“^“符号是异或运算
    return 9 * count

def DigitAtIndex(index, digits):
    number = beginNumber(digits) + index // digits
    indexFromRight = digits - index % digits
    for i in range(1, indexFromRight):
        number //= 10
    return number % 10

def beginNumber(digits):
    if digits == 1:
        return 0

    return 10 ** (digits -1)

if __name__ == '__main__':
    t = digitAtIndex(19)
    print(t)
