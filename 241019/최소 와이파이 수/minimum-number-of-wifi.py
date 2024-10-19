n,m=map(int,input().split())
l=list(map(int,input().split()))
x=0
st, val = 0, 0

while st < n:
    if l[st] == 1:
        val +=1
    
    if val == m:
        x += 1
        st += m + 1
        val = 0

    st += 1

if val:
    x += 1

print(x)