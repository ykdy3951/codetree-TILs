class Person:
    def __init__(self, name, a, b):
        self.name = name
        self.a = int(a)
        self.b = int(b)

    def __str__(self):
        return f"{self.name} {self.a} {self.b}"

print('\n'.join(map(str, sorted([Person(*input().split()) for _ in range(int(input()))], key=lambda x : (x.a, -x.b)))))