l=[input() for _ in range(int(input()))]
print(sum([len(x) for x in l]), ''.join(map(lambda x: x[0], l)).count('a'))