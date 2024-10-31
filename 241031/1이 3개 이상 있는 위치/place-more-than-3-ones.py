n=int(input())
l=[list(map(int,input())) for i in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
ans = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            if i + dx[k] < 0 or i + dx[k] >= n:
                continue
            if j + dy[k] < 0 or j + dy[k] >= n:
                continue
            
            nx, ny = i + dx[k], j + dy[k]
            cnt += l[nx][ny]
        ans += int(cnt >= 3)
print(ans)