def lcm(n : int, m : int) -> int:
    
    _n, _m = n, m
    if _n > _m:
        _n, _m = _m, _n

    while _n and _m:
        _m %= _n

        if _n > _m:
            _n, _m = _m, _n

    return n * m // _m

n, m = map(int,input().split())
print(lcm(n, m))