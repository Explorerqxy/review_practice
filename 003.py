#二位数组中的查找
def Find(matrix, rows, columns, number):
    found = False
    if matrix != None and rows > 0 and columns > 0:
        row = 0
        column = columns -1
        while row < rows and column >= 0:
            if matrix[row*column + column] == number:
                found = True
                break
            elif matrix[row*column + column] > number:
                column -= 1
            else:
                row += 1
    return found
