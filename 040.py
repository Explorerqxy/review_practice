def GetTranslationCount(number):
    if number < 0:
        return 0
    numberInString = str(number)
    return getTranslationCount(numberInString)

def getTranslationCount(number):
    length = len(number)
    counts = [0 for _ in range(length)]
    count = 0
    for i in range(length-1, -1, -1):
        count = 0
        if i < length - 1:
            count = counts[i+1]
        else:
            count = 1
        if i < length - 1:
            digit1 = ord(number[i]) - ord('0')
            digit2 = ord(number[i+1]) - ord('0')
            converted = digit1 * 10 + digit2
            if converted >= 10 and converted <= 25:
                if i < length -2:
                    count += counts[i+2]
                else:
                    count += 1
        counts[i] = count
    count = counts[0]
    return count

if __name__ == '__main__':
    a = 12258
    t = GetTranslationCount(a)
    print(t)