class Test:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        return f"code : {self.a}\ncolor : {self.b}\nsecond : {self.c}"

print(Test(*input().split()))