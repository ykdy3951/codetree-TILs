def count_valid_pairs(A):
    stack = []
    count = 0

    for char in A:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if len(stack) >= 2:
                stack.pop()
                stack.pop()
                count += 1
    return count

A = input()
print(count_valid_pairs(A)*2)