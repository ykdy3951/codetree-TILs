"""
Problem Summary
1. 2n -> n개의 묶음
2. 각 그룹의 수 차이의 최솟값이 최대

그룹 간의 수 차이가 비슷하게 가지고 가야함
"""

n=int(input())
l=sorted(map(int,input().split()))
ans=1e12
for i in range(n):
    ans=min(l[i+n]-l[i], ans)
print(ans)