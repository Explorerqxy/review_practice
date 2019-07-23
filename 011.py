def maxProductAfterCutting_solution1(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    products = [0 for _ in range(length+1)]
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    max = 0
    for i in range(4, length+1):
        max = 0
        for j in range(1, i//2+1):
            product = products[j] * products[i-j]
            if max < product:
                max = product
            products[i] = max
    max = products[length]
    return max

def maxProductAfterCutting_solution2(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    #尽可能多的剪去长度为3的绳子段
    timesOf3 = length // 3
    #当绳子最后剩下的长度为4的时候， 不能再剪去长度为3的绳子段
    #此时更好的方法是把绳子剪成长度为2的两段，因为2*2>3*1
    if length - timesOf3*3 ==1:
        timesOf3 -= 1
    timesOf2 = (length - timesOf3*3)//2
    return 3**timesOf3 * 2**timesOf2

if  __name__ == '__main__':
    a = maxProductAfterCutting_solution2(10)
    b = maxProductAfterCutting_solution1(10)
    print(a)
    print(b)
