n = int(input())
s = input()

count_c = 0
count_co = 0
count_cow = 0

for char in s:
    if char == 'C':
        count_c += 1
    elif char == 'O':
        count_co += count_c
    elif char == 'W':
        count_cow += count_co

print(count_cow)