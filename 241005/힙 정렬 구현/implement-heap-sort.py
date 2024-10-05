import heapq

n = int(input())
h = list(map(int,input().split()))

heapq.heapify(h)

while h:
  print(heapq.heappop(h), end=' ')