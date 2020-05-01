#替换空格
def ReplaceBlank(string, length):
    if string == None or length <= 0:
        return

    originalLength = len(string)
    numberOfBlank = 0
    i = 0
    while i != originalLength:
        if string[i] == " ":
            numberOfBlank += 1
        i += 1

    newLength = originalLength + numberOfBlank *2
    if newLength > length :
        return
    indexOfOriginal = originalLength
    indexOfNew = newLength
    while indexOfOriginal >= 0 and indexOfNew > indexOfOriginal:
        if string[indexOfOriginal] == " ":
            string[indexOfNew] = '0'
            indexOfNew -= 1
            string[indexOfNew] = '2'
            indexOfNew -= 1
            string[indexOfNew] = '%'
            indexOfNew -= 1
        else:
            string[indexOfNew] = string[indexOfOriginal]
            indexOfNew -= 1
        indexOfOriginal -= 1

