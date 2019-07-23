def Print1ToMaxOfNDigits(n):
    if n <= 0:
        return
    number = ['0' for _ in range(n)]
    for i in range(10):
        number[0] = str(i)
        Print1ToMaxOfNDigitsRecuisively(number, n, 0)

def Print1ToMaxOfNDigitsRecuisively(number, length, index):
    if index == length - 1:
        PrintNumber(number)
        return
    for i in range(10):
        number[index+1] = str(i)
        Print1ToMaxOfNDigitsRecuisively(number, length, index+1)

def PrintNumber(number):
    #isBeginning0 = True
    #nLength = len(number)
    res = ''.join(number)
    s = res.lstrip('0')
    print(s)

if __name__ == '__main__':
    Print1ToMaxOfNDigits(3)