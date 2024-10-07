N = int(input())
CENTER = 100000
t = 0
cnt = [[-1,0] for _ in range(2 * CENTER + 5)]
for i in range(N):
    x, y = input().split()
    x = int(x)

    if y == 'L':
        for j in range(t, t-x, -1):
            if cnt[j + CENTER][1] >= 3:
                cnt[j + CENTER] = [2, 4]
            else:
                cnt[j + CENTER] = [0, cnt[j + CENTER][1] + 1]
        t = t-x+1
    else:
        for j in range(t, t+x):
            if cnt[j + CENTER][1] >= 3:
                cnt[j + CENTER] = [2, 4]
            else:
                cnt[j + CENTER] = [1, cnt[j + CENTER][1] + 1]
        t = t+x-1

ans = [0] * 3
for i in range(2 * CENTER + 5):
    if cnt[i][0] >= 0:
        ans[cnt[i][0]] += 1
print(*ans)