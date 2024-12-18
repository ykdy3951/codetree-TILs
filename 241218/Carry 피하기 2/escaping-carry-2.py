from itertools import combinations

def has_no_carry(x, y, z):
    x, y, z = str(x), str(y), str(z)
    max_len = max(len(x), len(y), len(z))
    x, y, z = x.zfill(max_len), y.zfill(max_len), z.zfill(max_len)
    
    for i in range(max_len):
        if int(x[i]) + int(y[i]) + int(z[i]) >= 10:
            return False
    return True

def max_sum_no_carry(numbers):
    max_sum = -1
    for comb in combinations(numbers, 3):
        if has_no_carry(*comb):
            max_sum = max(max_sum, sum(comb))
    return max_sum

n = int(input())
numbers = [int(input()) for _ in range(n)]
print(max_sum_no_carry(numbers))