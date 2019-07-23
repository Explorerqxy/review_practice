def PowerWithUnsignedExponent(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = PowerWithUnsignedExponent(base, exponent >> 1)
    result *= result
    if exponent & 0x1 == 1:
        result *= base
    return result

if __name__ == '__main__':
    a = PowerWithUnsignedExponent(3,2)
    print(a)