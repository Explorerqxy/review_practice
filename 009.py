def hasPath(matrix, rows, cols, str):
    if matrix == None or rows < 1 or cols < 1 or str == None:
        return False

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    pathLength = 0
    for row in range(rows):
        for col in range(cols):
            if hasPathCore(matrix, rows, cols,row, col, str, pathLength, visited):
                return True
    return False

def hasPathCore(matrix, rows, cols, row, col, str, pathLength, visited):
    if pathLength == len(str):
        return True
    hasPath = False
    if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row*cols + col] == str[pathLength] and not visited[row][col]:
        pathLength += 1
        visited[row][col] = True

        hasPath = hasPathCore(matrix, rows, cols, row, col-1, str, pathLength, visited) \
                or hasPathCore(matrix, rows, cols, row-1, col, str, pathLength, visited) \
                or hasPathCore(matrix, rows, cols, row, col+1, str, pathLength, visited) \
                or hasPathCore(matrix, rows, cols, row+1, col, str, pathLength, visited)

        if not hasPath:
            pathLength -= 1
            visited[row][col] = False
    return hasPath

if __name__ == '__main__':
    m = ['a', 'b', 't', 'g', 'c', 'f', 'c', 's', 'j', 'd', 'e','h']
    s = 'cfdeh'
    a = hasPath(m, 3, 4, s)
    print(a)