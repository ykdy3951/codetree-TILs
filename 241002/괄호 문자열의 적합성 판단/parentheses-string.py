from collections import deque

def solve(s : str) -> bool:
    d = deque()
    for i in s:
        if i == '(':
            d.append(i)
        else:
            if not len(d):
                return False
            d.pop()
    if len(d):
        return False
    return True

print(['No','Yes'][solve(input())])