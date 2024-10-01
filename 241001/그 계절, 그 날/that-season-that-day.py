def is_leap(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    return False

def is_valid_day(y, m, d):
    if m > 12:
        return False

    if m == 2:
        if is_leap(y):
            return d < 30
        else:
            return d < 29
    
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        return d < 32

    else:
        return d < 31

def solve(y, m, d):
    if is_valid_day(y, m, d):
        print(['Spring', 'Summer', 'Fall', 'Winter'][((m + 9) % 12) // 3])
    else:
        print(-1)

y,m,d=map(int,input().split())
solve(y, m, d)