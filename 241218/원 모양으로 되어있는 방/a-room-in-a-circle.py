N = int(input())
people = [int(input()) for _ in range(N)]

prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + people[i - 1]

min_distance_sum = float('inf')

for start in range(N):
    distance_sum = 0
    for i in range(N):
        distance = (i - start) if i >= start else (i + N - start)
        distance_sum += distance * people[i]
    min_distance_sum = min(min_distance_sum, distance_sum)

print(min_distance_sum)