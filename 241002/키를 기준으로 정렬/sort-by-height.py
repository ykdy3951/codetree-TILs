class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = int(h)
        self.w = int(w)

    def __str__(self):
        return f"{self.name} {self.h} {self.w}"

print('\n'.join(map(str, sorted([Person(*input().split()) for _ in range(int(input()))], key=lambda x: x.h))))