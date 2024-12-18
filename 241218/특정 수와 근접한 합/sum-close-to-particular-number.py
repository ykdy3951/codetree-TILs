from itertools import combinations

def closest_sum_difference(N, S, numbers):
    total_sum = sum(numbers)
    closest_diff = float('inf')

    for comb in combinations(numbers, 2):
        excluded_sum = total_sum - sum(comb)
        closest_diff = min(closest_diff, abs(S - excluded_sum))

    return closest_diff

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
print(closest_sum_difference(N, S, numbers))