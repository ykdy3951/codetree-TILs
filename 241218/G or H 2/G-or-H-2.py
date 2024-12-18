def read_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])
    people = []
    for i in range(1, N + 1):
        position, label = data[i].split()
        people.append((int(position), label))
    return N, people

def max_photo_size(N, people):
    people.sort()
    max_size = 0

    for i in range(N):
        g_count = 0
        h_count = 0
        for j in range(i, N):
            if people[j][1] == 'G':
                g_count += 1
            else:
                h_count += 1

            if g_count == 0 or h_count == 0 or g_count == h_count:
                max_size = max(max_size, people[j][0] - people[i][0])

    return max_size

def main():
    N, people = read_input()
    result = max_photo_size(N, people)
    print(result)

if __name__ == "__main__":
    main()
