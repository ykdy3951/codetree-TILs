def read_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])
    a, b, c = map(int, data[1].split())
    return N, a, b, c

def is_within_distance(x, y):
    return abs(x - y) <= 2

def count_unlock_combinations(N, a, b, c):
    count = 0

    for x in range(1, N + 1):
        for y in range(1, N + 1):
            for z in range(1, N + 1):
                if (
                    is_within_distance(x, a) or
                    is_within_distance(y, b) or
                    is_within_distance(z, c)
                ):
                    count += 1

    return count

def main():
    N, a, b, c = read_input()
    result = count_unlock_combinations(N, a, b, c)
    print(result)

if __name__ == "__main__":
    main()
