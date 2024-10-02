class Person:
    def __init__(self, name, addr, region):
        self.name = name
        self.addr = addr
        self.region = region

    def __str__(self):
        return f'name {self.name}\naddr {self.addr}\ncity {self.region}'
    
print(sorted([Person(*input().split()) for _ in range(int(input()))], key=lambda x : x.name)[-1])