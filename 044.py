def FirstNotRepeatingChar(Spring):
    if Spring == None:
        return None
    dic = {}
    length = len(Spring)
    for i in range(length):
        if Spring[i] in dic:
            dic[Spring[i]] += 1
        else:
            dic[Spring[i]] = 1
    for i in range(length):
        if dic[Spring[i]] == 1:
            return Spring[i]
    return None

if __name__ == '__main__':
    t = FirstNotRepeatingChar("abacdeff")
    print(t)
