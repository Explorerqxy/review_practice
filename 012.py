def NumberOf1(n):
    count = 0
    while n:
        if n & 1:
            count += 1
        n = n >> 1
    return count

def NumberOf1_(n):
    count = 0
    flag = 1
    while flag:
        if n & flag:
            count += 1
        flag = flag << 1
    return count
#python int 无限大，没法用32位约束

def NumberOf1__(n):
    count = 0
    while n:
        count += 1
        n = (n-1) & n
    return count


if __name__ == '__main__':
    a = NumberOf1__(9)
    print(a)