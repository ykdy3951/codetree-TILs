class Point:
    def __init__(self, x, y, idx):
        self.x = int(x)
        self.y = int(y)
        self.idx = int(idx)


    def __str__(self):
        return f"{self.idx}"

print('\n'.join(map(str, sorted([Point(*input().split(), _+1) for _ in range(int(input()))], key=lambda x: (abs(x.x) + abs(x.y), x.idx)))))