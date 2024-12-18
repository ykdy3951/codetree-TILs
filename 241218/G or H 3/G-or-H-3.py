def max_score(N, K, people):
    people.sort()
    max_score = 0
    current_score = 0
    left = 0

    for right in range(N):
        position, letter = people[right]
        current_score += 1 if letter == 'G' else 2

        while position - people[left][0] > K:
            current_score -= 1 if people[left][1] == 'G' else 2
            left += 1

        max_score = max(max_score, current_score)

    return max_score

N, K = map(int, input().split())
people = [tuple(input().split()) for _ in range(N)]
people = [(int(pos), char) for pos, char in people]
print(max_score(N, K, people))