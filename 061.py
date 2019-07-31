def Add(num1, num2):
    while num2 != 0:
        sum = num1 ^ num2
        carry = (num1 & num2) << 1
        num1 = sum
        num2 = carry
    return num1

if __name__ == '__main__':
    t = Add(3,4)
    print(t)