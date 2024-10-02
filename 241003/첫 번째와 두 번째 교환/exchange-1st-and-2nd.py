s=list(input())
a,b=s[0],s[1]
print(''.join(map(lambda x: a if x == b else b if x == a else x, s)))