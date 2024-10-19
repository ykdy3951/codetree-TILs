n=int(input())
l=[int(input()) for _ in range(n)]
target=sum(l)//n
ans=0
for i in l:
    ans += abs(i - target)
print(ans//2)