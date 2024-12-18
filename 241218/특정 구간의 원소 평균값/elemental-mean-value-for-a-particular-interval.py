def count_valid_intervals(N, numbers):
    valid_counts = set()

    for start in range(N):
        total_sum = 0
        for end in range(start, N):
            total_sum += numbers[end]
            length = end - start + 1
            if total_sum % length == 0:
                avg = total_sum // length
                if avg in numbers[start:end + 1]:
                    valid_counts.add((start, end))

    return len(valid_counts)

N = int(input())
numbers = list(map(int, input().split()))
print(count_valid_intervals(N, numbers))