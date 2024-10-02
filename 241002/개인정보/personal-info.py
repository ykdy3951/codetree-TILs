class Person:
    def __init__(self, name, a, b):
        self.name = name
        self.a = int(a)
        self.b = float(b)

    def __str__(self):
        return f"{self.name} {self.a} {self.b:.1f}"

l = [Person(*input().split()) for _ in range(5)]

print("name")
print('\n'.join(map(str, sorted(l, key=lambda x : x.name))))

print("\nheight")
print('\n'.join(map(str, sorted(l, key=lambda x : -x.a))))