from collections import deque
n,k=map(int,input().split())

l = deque()
arr = []

for i in range(n):
    l.append(i+1)

while len(l) != 1:
    for i in range(k-1):
        l.append(l.popleft())
    arr.append(l.popleft())
arr.append(l.popleft())
print(*arr)