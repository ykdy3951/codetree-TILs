def read_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])
    a1, b1, c1 = map(int, data[1].split())
    a2, b2, c2 = map(int, data[2].split())
    return N, (a1, b1, c1), (a2, b2, c2)

def is_within_distance(x, y, N):
    return abs(x - y) <= 2 or abs(x - y) >= N - 2

def count_unlock_combinations(N, combo1, combo2):
    count = 0

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                if (
                    (is_within_distance(x, combo1[0], N) and
                        is_within_distance(y, combo1[1], N) and
                        is_within_distance(z, combo1[2], N)) or
                    (is_within_distance(x, combo2[0], N) and 
                        is_within_distance(y, combo2[1], N) and 
                        is_within_distance(z, combo2[2], N))
                ):
                    count += 1

    return count

def main():
    N, combo1, combo2 = read_input()
    result = count_unlock_combinations(N, combo1, combo2)
    print(result)

if __name__ == "__main__":
    main()