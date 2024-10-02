class User:
    def __init__(self, id, lv):
        self.id = id
        self.lv = lv

    def __str__(self):
        return f"user {self.id} lv {self.lv}"

a = User("codetree", 10)
b = User(*input().split())

print(a)
print(b)