n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

def can_all_overlap_excluding_one(segments):
    for i in range(len(segments)):
        remaining_segments = segments[:i] + segments[i+1:]
        overlap_start = remaining_segments[0][0]
        overlap_end = remaining_segments[0][1]
        
        for x1, x2 in remaining_segments:
            overlap_start = max(overlap_start, x1)
            overlap_end = min(overlap_end, x2)
        
        if overlap_start <= overlap_end:
            return True
    return False

if can_all_overlap_excluding_one(segments):
    print("Yes")
else:
    print("No")