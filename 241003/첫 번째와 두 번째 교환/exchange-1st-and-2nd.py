s=input()
a,b=s[0],s[1]
s=s.replace(b,a)
s=s.replace(a,b)
print(b+a+s[2:])