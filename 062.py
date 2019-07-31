def multiply(array1, array2):
    length1 = len(array1)
    length2 = len(array2)
    if length1 == length2 and length2 > 1:
        array2[0] = 1
        for i in range(1, length1):
            array2[i] = array2[i -1] * array1[i -1]

        tmp = 1
        for i in range(length1 -2, -1,-1):
            tmp *= array1[i+1]
            array2[i] *= tmp

def JC(n):
    if n == 0:
        return 1
    return n * JC(n-1)

if __name__ == '__main__':
    array1 = [1,2,3,4,5,6,7]
    array2 = [1,1,1,1,1,1,1]
    multiply(array1,array2)
    print(array2)

    print(JC(7))