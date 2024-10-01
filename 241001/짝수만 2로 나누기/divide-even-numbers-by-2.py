def solve(l : list) -> None:
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] //= 2

n=int(input())
l=list(map(int,input().split()))
solve(l)
print(' '.join(map(str, l)))