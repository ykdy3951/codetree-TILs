class Test:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return f"secret code : {self.a}\nmeeting point : {self.b}\ntime : {self.c}"

print(Test(*input().split()))