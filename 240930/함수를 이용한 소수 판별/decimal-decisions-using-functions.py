from math import *
def sum_prime_with_range(a, b):
    ans = 0
    is_prime = [True] * (b+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(sqrt(b)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i*i, b+1, i):
            is_prime[j] = False

    for i in range(a, b + 1):
        if is_prime[i]:
            ans += i

    return ans

a,b = map(int,input().split())
print(sum_prime_with_range(a, b))