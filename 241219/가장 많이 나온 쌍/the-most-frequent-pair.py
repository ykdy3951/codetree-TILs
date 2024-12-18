def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    n, m = map(int, data[0].split())
    pairs = [tuple(sorted(map(int, line.split()))) for line in data[1:]]
    return n, m, pairs

def most_frequent_pair(n, m, pairs):
    pair_counts = {}

    for pair in pairs:
        if pair in pair_counts:
            pair_counts[pair] += 1
        else:
            pair_counts[pair] = 1

    return max(pair_counts.values())

def main():
    n, m, pairs = read_input()
    result = most_frequent_pair(n, m, pairs)
    print(result)

if __name__ == "__main__":
    main()
