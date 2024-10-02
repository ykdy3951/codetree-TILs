class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f"product {self.b} is {self.a}"

print(Test("codetree", 50))
print(Test(*input().split()))