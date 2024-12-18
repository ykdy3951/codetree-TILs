N, K, P, T = map(int, input().split())

infected = [0 for _ in range(N + 1)]
infection_count = [0 for _ in range(N + 1)]

handshakes = [list(map(int, input().split())) for _ in range(T)]
handshakes.sort(key=lambda x: x[0])

infected[P] = 1
infection_count[P] = K

for handshake in handshakes:
    person1, person2 = handshake[1], handshake[2]
    if infected[person1] and infection_count[person1] > 0 and not infected[person2]:
        infected[person2] = 1
        infection_count[person1] -= 1
        infection_count[person2] = K
    elif infected[person2] and infection_count[person2] > 0 and not infected[person1]:
        infected[person1] = 1
        infection_count[person2] -= 1
        infection_count[person1] = K
    elif infected[person1] and infected[person2]:
        if infection_count[person1] > 0:
            infection_count[person1] -= 1
        if infection_count[person2] > 0:
            infection_count[person2] -= 1

print(''.join(map(str, infected[1:])))