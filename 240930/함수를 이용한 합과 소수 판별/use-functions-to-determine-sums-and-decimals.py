from math import sqrt
def solve(a, b):
    prime_list = [1] * (b+1)

    prime_list[0] = prime_list[1] = 0
    for i in range(2, int(sqrt(b))+1):
        if not prime_list[i]:
            continue
        for j in range(i*i, b+1, i):
            prime_list[j] = 0
    
    ans = 0
    for i in range(a, b+1):
        if prime_list[i] and sum(map(int,list(str(i)))) % 2 == 0:
            ans += 1
    return ans

a, b = map(int, input().split())
print(solve(a, b))