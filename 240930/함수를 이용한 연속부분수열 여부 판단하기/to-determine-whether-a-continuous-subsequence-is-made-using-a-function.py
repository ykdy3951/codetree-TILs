n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for i in range(len(x)-len(y)+1):
    if x[i] == y[0]:
        flag = True
        for j in range(1,len(y)):
            if x[i+j] != y[j]:
                flag = False
                break
        if flag:
            print('Yes')
            exit()
print('No')