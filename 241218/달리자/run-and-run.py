n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_distance = 0
current_people = 0

for i in range(n):
    current_people += A[i] - B[i]
    total_distance += abs(current_people)

print(total_distance)