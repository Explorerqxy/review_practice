def ReverseSentence(Data):
    lst = Data.split(' ')
    lst.reverse()
    return ' '.join(lst)

if __name__ == '__main__':
    s = 'I am a student.'
    t = ReverseSentence(s)
    print(t)