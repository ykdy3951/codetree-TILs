n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

overlap_start = segments[0][0]
overlap_end = segments[0][1]

for x1, x2 in segments:
    overlap_start = max(overlap_start, x1)
    overlap_end = min(overlap_end, x2)

if overlap_start <= overlap_end:
    print("Yes")
else:
    print("No")