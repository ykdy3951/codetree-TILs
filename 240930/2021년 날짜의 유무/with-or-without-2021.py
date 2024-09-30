def solve(m,d) -> bool:
    if m > 12:
        return False
    if m == 2:
        return d < 29
    elif m in [1,3,5,7,8,10,12]:
        return d < 32
    else:
        return d < 30


m,d=map(int,input().split())
print(['No','Yes'][solve(m,d)])