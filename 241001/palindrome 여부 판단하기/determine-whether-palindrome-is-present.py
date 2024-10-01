def solve(a : str) -> bool:
    return a == a[::-1]

print(['No','Yes'][solve(input())])