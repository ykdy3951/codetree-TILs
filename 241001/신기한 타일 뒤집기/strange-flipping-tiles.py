n = int(input())
l = [0, 0]
for _ in range(n):
    x, cnt = input().split()
    x = int(x)
    cnt = 1 if cnt == 'L' else 2
    
    l[cnt-1] += x
    l[2-cnt] = max(0, l[2-cnt]-x)
print(l[0], l[1])