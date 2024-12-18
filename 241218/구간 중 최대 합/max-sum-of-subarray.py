def max_sum_of_k_consecutive(n, k, numbers):
    current_sum = sum(numbers[:k])
    max_sum = current_sum

    for i in range(k, n):
        current_sum += numbers[i] - numbers[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
print(max_sum_of_k_consecutive(n, k, numbers))