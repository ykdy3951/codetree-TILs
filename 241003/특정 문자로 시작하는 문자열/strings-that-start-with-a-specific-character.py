l=[input() for _ in range(int(input()))];e=input()
l=list(filter(lambda x : x[0] == e, l))
print(f"{len(l)} {sum(map(lambda x: len(x), l)) / len(l):.2f}")