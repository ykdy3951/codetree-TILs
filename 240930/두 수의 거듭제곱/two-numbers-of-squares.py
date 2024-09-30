l = [0] * 11
l[0] = 1
def _pow(a, b):
    global l
    if b == 0:
        return 1
    if l[b]:
        return l[b]
    if b % 2:
        l[b] = a * _pow(a, b // 2) * _pow(a, b // 2)
        return l[b]
    l[b] = _pow(a, b // 2) * _pow(a, b // 2)
    return l[b]

a, b = map(int, input().split())
print(_pow(a, b))