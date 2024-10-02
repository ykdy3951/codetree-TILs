a,b=input(),input();s=0
for i in range(len(a)-len(b)+1):
    if a[i:i+len(b)] == b:
        s+=1
print(s)