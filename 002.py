def getDuplication(numbers, length):
    if numbers == None or length <= 0:
        return -1
    start = 1
    end = length -1
    while end >= start:
        middle = ((end-start)>>1) + start
        count= countRange(numbers, length, start, middle)
        if end == start:
            if count > 1:
                return start
            else:
                break
        if count > (middle - start +1):
            end = middle
        else:
            start = middle + 1
    return -1

def countRange(numbers, length, start, end):
    if numbers == None:
        return 0
    count = 0
    for i in range(length):
        if numbers[i] >= start and numbers[i] <= end:
            count += 1
    return count

if __name__ == "__main__":
    a = getDuplication([2,3,5,4,3,2,6,7],8)
    print(a)
