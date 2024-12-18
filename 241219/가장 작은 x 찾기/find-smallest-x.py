def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    n = int(data[0])
    ranges = [tuple(map(int, line.split())) for line in data[1:]]
    return n, ranges

def find_minimum_x(n, ranges):
    from math import ceil, floor
    min_x, max_x = ranges[0] 
    dom = 2
    min_x = int(ceil(min_x / 2))
    max_x = int(floor(max_x / 2))

    for i in range(1, n):
        a, b = ranges[i]
        dom *= 2
        min_x = max(min_x, int(ceil(a / dom)))
        max_x = min(max_x, int(floor(b / dom)))

    return min_x

def main():
    n, ranges = read_input()
    result = find_minimum_x(n, ranges)
    print(result)

if __name__ == "__main__":
    main()