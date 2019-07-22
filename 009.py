def hasPath(matrix, rows, cols, str):
    if matrix == None or rows < 1 or cols < 1 or str == None:
        return False

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    pathLength = 0
    