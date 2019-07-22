def SortAges(ages, length):
    if ages == None or length <= 0:
        return
    oldestAge = 99
    timesOfAge = [0 for i in range(oldestAge+1)]

    for i in range(length):
        age = ages[i]
        if age < 0 or age > oldestAge:
            return None
        timesOfAge[age] += 1

    index = 0
    for i in range(oldestAge+1):
        for j in range(timesOfAge[i]):
            ages[index] = i
            index += 1

if __name__ == '__main__':
    t = [i for i in range(100)]
    for i in range(3):
        t[i] = 15
    for i in range(5,9):
        t[i] = 3
    SortAges(t,100)
    print(t)