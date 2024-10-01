n = int(input())
l = list(map(int, input().split()))

for i in range(0, n, 2):
    print(sorted(l[:i+1])[i//2], end=' ')