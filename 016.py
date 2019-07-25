import re
def a(s):
    pattern = re.compile(r'\d+')
    m = pattern.match(s, 3, 10)
    print(m)

if __name__ == '__main__':
    s = 'one134nska324en56'
    a(s)