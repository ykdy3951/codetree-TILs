l = [list(map(int,input().split())) for _ in range(int(input()))]
cnt = [0] * (201)
m = 0
for i in l:
    for j in range(i[0], i[1]):
        cnt[j + 100] += 1
        m = max(cnt[j + 100], m)

print(m)