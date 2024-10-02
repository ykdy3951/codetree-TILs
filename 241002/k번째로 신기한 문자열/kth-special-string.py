n, k, t = input().split()
l = sorted(filter(lambda x : x[:len(t)] == t, [input() for _ in range(int(n))]))
print(l[int(k)-1])