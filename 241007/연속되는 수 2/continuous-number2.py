n=int(input())
prev = -1
cnt = 0
ans = 0 
for i in range(n):
    x = int(input())
    if x != prev:
        ans = max(ans, cnt)
        prev = x
        cnt = 1
    else:
        cnt += 1

print(max(ans, cnt))