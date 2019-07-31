def FindNumberAppearingOnce(numbers, length):
    if numbers == None or length <= 0:
        return
    bitSum = [0 for _ in range(32)]
    for i in range(length):
        bitMask = 1
        for j in range(31, -1, -1):
            bit = numbers[i] & bitMask
            if bit != 0:
                bitSum[j] += 1
            bitMask = bitMask << 1
    result = 0
    for i in range(32):
        result = result << 1
        result = bitSum[i] % 3
    return result


#因为数字表示方式不同，本算法目前只适合C++
if __name__ == '__main__':
    a = [1,2,3,1,2,3,1,2,3,5,6,5,6,5]
    t = FindNumberAppearingOnce(a,14)
    print(t)
