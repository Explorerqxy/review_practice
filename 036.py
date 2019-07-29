import importlib
m = importlib.import_module("006")
def GetLeastNUmbers(input, n, output, k):
    if input == None or output == None or k > n or n <= 0 or k <= 0:
        return
    start = 0
    end = n-1
    index = m.Partition(input, n, start, end)
    while index != k-1:
        if index > k-1:
            index = m.Partition(input, n, start, index-1)
        else:
            start = index + 1
            index = m.Partition(input, n, start, end)
    for i in range(k):
        output.append(input[i])

