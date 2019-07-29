def longestSubstringWithoutDuplication(str):
    curLength = 0
    maxLength = 0
    position = [-1 for _ in range(26)]
    for i in range(len(str)):
        prevIndex = position[ord(str[i]) - ord('a')]
        if prevIndex < 0 or i - prevIndex > curLength:
            curLength += 1
        else:
            if curLength > maxLength:
                maxLength = curLength
            curLength = i - prevIndex
        position[ord(str[i]) - ord('a')] = i
    if curLength > maxLength:
        maxLength = curLength
    return maxLength

if __name__ == '__main__':
    a = "arabcacfr"
    t = longestSubstringWithoutDuplication(a)
    print(t)