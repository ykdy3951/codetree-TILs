n=input()
if int(n) % 2 == 0 and sum(map(int,list(n))) % 5 == 0:
    print('Yes')
else:
    print('No')