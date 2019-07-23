def movinigCount(threshold, rows, cols):
    if threshold < 0 or rows <= 0 or cols <= 0:
        return 0

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    count = movingCountCore(threshold, rows, cols, 0, 0, visited)

    return count

def movingCountCore(threshold, rows, cols, row, col, visited):
    count = 0
    if check(threshold, rows, cols, row, col, visited):
        visited[row][col] = True

        count = 1 + movingCountCore(threshold, rows, cols, row-1, col, visited) \
                + movingCountCore(threshold, rows, cols, row, col-1, visited) \
                + movingCountCore(threshold, rows, cols, row+1, col, visited) \
                + movingCountCore(threshold, rows, cols, row, col+1, visited)
    return count

def check(threshold, rows, cols, row, col, visited):
    if row >= 0 and row < rows and col >= 0 and col < cols and getDigitSum(row) + getDigitSum(col) <= threshold and not visited[row][col]:
        return True
    return False

def getDigitSum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum

if __name__ == '__main__':
    a = movinigCount(5,10,10)
    print(a)