def count_valid_pairs(A):
    n = len(A)
    count = 0
    for i in range(n - 3):
        if A[i] == '(' and A[i + 1] == '(':
            for j in range(i + 2, n - 1):
                if A[j] == ')' and A[j + 1] == ')':
                    count += 1
    return count
A = input()
print(count_valid_pairs(A))