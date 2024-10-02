s=list(input())
while len(s) > 1:
    n = int(input())
    if n >= len(s):
        del s[-1]
    else:
        del s[n]
    print(''.join(s))