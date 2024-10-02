class Person:
    def __init__(self, a, b, idx):
        self.a = int(a)
        self.b = int(b)
        self.idx = int(idx)

    def __str__(self):
        return f"{self.a} {self.b} {self.idx}"

print('\n'.join(map(str, sorted([Person(*input().split(), _+1) for _ in range(int(input()))], key=lambda x : (-x.a, -x.b, x.idx)))))