N = int(input())
CENTER = 100000
t = 0
l = []
cnt = [0] * (2 * CENTER + 5)
for i in range(N):
    x, y = input().split()
    x = int(x)

    if y == 'L':
        l.append([t-x+1, t])
        t = t-x+1
    else:
        l.append([t, t+x-1])
        t = t+x-1

for i in l:
    for j in range(i[0], i[1]+1):
        cnt[j + CENTER] += 1

ans = [0] *3
for i in range(2 * CENTER + 5):
    if i - CENTER < 0:
        if cnt[i] > 3:
            ans[2] += 1
        elif cnt[i] > 0:
            ans[1 - (cnt[i] % 2)] += 1
    elif i == CENTER:
        if cnt[i] > 3:
            ans[2] += 1
        elif l[0][0]:
            ans[1 - (cnt[i] % 2)] += 1
        else:
            ans[cnt[i] % 2] += 1
    else:
        if cnt[i] > 3:
            ans[2] += 1
        elif cnt[i] > 0:
            ans[cnt[i] % 2] += 1
print(*ans)