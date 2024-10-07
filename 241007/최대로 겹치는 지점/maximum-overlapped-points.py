l = [list(map(int,input().split())) for _ in range(int(input()))]
cnt = [0] * 105
m = 0
for i in l:
    for j in range(i[0], i[1] + 1):
        cnt[j] += 1
        m = max(cnt[j], m)

print(m)