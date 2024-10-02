n=int(input())
print(*map(lambda x : x[2], sorted([[i+1]+x for i, x enumerate(sorted([[b, a+1] for a, b in enumerate(map(int,input().split()))], key=lambda x: (x[0], x[1])))], key=lambda x: x[0])))