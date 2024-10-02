s=input()
a=''
x,y=s[0],1
for i in s[1:]:
    if i != x:
        a += x + str(y)
        x, y = i, 1
        continue
    y += 1
a += x + str(y)
print(len(a), a, sep='\n')