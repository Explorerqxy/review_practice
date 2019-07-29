def getMaxValue_solution1(values, rows, cols):
    if values == None or rows <= 0 or cols <= 0:
        return 0
    maxValues = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            left = 0
            up = 0
            if i > 0:
                up = maxValues[i-1][j]
            if j > 0:
                left = maxValues[i][j-1]
            maxValues[i][j] = max(up, left) + values[i*cols + j]
    maxValue = maxValues[-1][-1]
    return maxValue

if __name__ == '__main__':
    a = [1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5]
    t = getMaxValue_solution1(a,4,4)
    print(t)