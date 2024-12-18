N = int(input())
pigeon_positions = {}
cross_count = 0
for _ in range(N):
    pigeon, position = map(int, input().split())
    if pigeon in pigeon_positions:
        if pigeon_positions[pigeon] != position:
            cross_count += 1
    pigeon_positions[pigeon] = position
print(cross_count)