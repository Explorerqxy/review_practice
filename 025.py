def PrintMatrixClockwisely(numbers, columns, rows):
    if numbers == None or columns <= 0 or rows <= 0:
        return
    start = 0
    while columns > start * 2 and rows > start * 2:
        PrintMatrixInCircle(numbers, columns, rows, start)
        start += 1

def PrintMatrixInCircle(numbers, columns, rows, start):
    endX = columns -1 - start
    endY = rows - 1 - start
    #从左到右打印一行
    for i in range(start, endX+1):
        number = numbers[start][i]
        printNumber(number)
    #从上到下打印一列
    if start < endY:
        for i in range(start+1, endY+1):
            number = numbers[i][endX]
    #从右到左打印一行
    if start < endX and start < endY:
        for i in range(endX-1, start-1, -1):
            number = numbers[endY][i]
            printNumber(number)
    #从下到上打印一列
    if start < endX and start < endY -1:
        for i in range(endY-1, start, -1):
            number = numbers[i][start]
            printNumber(number)

def printNumber(number):
    print(number)
