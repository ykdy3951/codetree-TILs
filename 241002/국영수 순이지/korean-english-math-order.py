class Person:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = int(kor)
        self.eng = int(eng)
        self.mat = int(mat)

    def __str__(self):
        return f"{self.name} {self.kor} {self.eng} {self.mat}"

print('\n'.join(map(str, sorted([Person(*input().split()) for _ in range(int(input()))], key=lambda x : (-x.kor, -x.eng, -x.mat)))))