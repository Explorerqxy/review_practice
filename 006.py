import random
def Partition(data, length, start, end):
    if data == None or length <= 0 or start <0 or end >= length:
        return None
    index = random.randint(start,end)
    data[index], data[end] = data[end], data[index]
    small = start - 1
    for index in range(start, end):
        if data[index] < data[end]:
            small += 1
            if small != index:
                data[small], data[index] = data[index], data[small]
    small += 1
    data[small], data[end] = data[end], data[small]
    return small

def QuickSort(data, length, start, end):
    if start == end :
        return
    index = Partition(data, length, start, end)
    if index > start:
        QuickSort(data, length, start, index-1)
    if index < end:
        QuickSort(data, length, index+1, end)

if __name__ == '__main__':
    a = [1,6,2,0,7,8,9,3,5,4]
    QuickSort(a,10,0,9)
    print(a)