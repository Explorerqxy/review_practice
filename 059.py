def LastRemaining(n, m):
    if n < 1 or m < 1:
        return -1
    i = 0
    numbers= []
    for i in range(n):
        numbers.append(i)
    current = 0
    while len(numbers) > 1:
        for i in range(1, m):
            current += 1
            if current == len(numbers):
                current = 0
        a = numbers.pop(current)
        #print(a)
        if current == len(numbers):
            current = 0
    return numbers[0]

def LastRemaining2(n, m):
    if n < 1 or m < 1:
        return -1
    last = 0
    for i in range(2, n + 1):
        last = (last + m) % i
    return last

if __name__ == '__main__':
    t = LastRemaining(5,3)
    print(t)
    p = LastRemaining2(5,3)
    print(p)

