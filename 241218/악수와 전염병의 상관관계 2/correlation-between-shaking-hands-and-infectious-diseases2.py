N, K, P, T = map(int, input().split())
P -= 1

handshakes = []
for i in range(1, T + 1):
    t, x, y = map(int, input().split())
    handshakes.append((t, x - 1, y - 1))
handshakes.sort()

infected = [0] * N
transmit_count = [0] * N
infected[P] = 1
transmit_count[P] = K

for _, x, y in handshakes:
    if infected[x] and transmit_count[x] > 0:
        if not infected[y]:
            infected[y] = 1
            transmit_count[y] = K
        transmit_count[x] -= 1

    if infected[y] and transmit_count[y] > 0:
        if not infected[x]:
            infected[x] = 1
            transmit_count[x] = K
        transmit_count[y] -= 1

print(''.join(map(str, infected)))