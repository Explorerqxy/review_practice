
def exam(score, number, student, q):
    res = []
    temp = score.sorted()
    for i in range(q):
        j = 0
        while temp[j] < score[student[i]]:
            j += 1
        j -= 1
        t = j/number
        re.append(t)
    return res
if __name__ == '__main__':
    number = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    score = list(map(int, line.split()))
    q = int(sys.stdin.readline().strip())
    student = []
    for i in range(q):
        line =  sys.stdin.readline().strip()
        values = line.split()
        student.append(values)
    res = exam(score, number, student,q)
    for i in range(res):
        prent(i)