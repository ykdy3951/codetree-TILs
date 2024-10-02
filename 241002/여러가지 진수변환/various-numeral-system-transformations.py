n,x=map(int,input().split())
s=''
while n:
    s += str(n % x)
    n //= x
print(s[::-1])