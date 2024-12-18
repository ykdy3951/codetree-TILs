from collections import Counter

def count_beautiful_subsequences(N, M, A, B):
    count_b = Counter(B)
    window_count = Counter(A[:M])
    beautiful_count = 0

    for i in range(N - M + 1):
        if i > 0:
            window_count[A[i - 1]] -= 1
            if window_count[A[i - 1]] == 0:
                del window_count[A[i - 1]]
            window_count[A[i + M - 1]] += 1

        if window_count == count_b:
            beautiful_count += 1

    return beautiful_count
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(count_beautiful_subsequences(N, M, A, B))