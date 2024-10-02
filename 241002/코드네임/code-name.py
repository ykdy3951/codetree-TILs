class Person:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} {self.b}"

l = sorted([Person(*input().split()) for _ in range(5)], key=lambda x : int(x.b))
print(l[0])