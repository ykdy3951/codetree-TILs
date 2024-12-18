def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    N, K = map(int, data[0].split())
    bombs = list(map(int, data[1:]))
    return N, K, bombs

def most_frequent_bomb(N, K, bombs):
    from collections import defaultdict

    frequency = defaultdict(int)

    for i in range(N):
        for j in range(i + 1, N):
            if abs(i - j) <= K and bombs[i] == bombs[j]:
                frequency[bombs[i]] += 1

    if not frequency:
        return 0

    max_frequency = max(frequency.values())
    candidates = [bomb for bomb, freq in frequency.items() if freq == max_frequency]

    return max(candidates)

def main():
    N, K, bombs = read_input()
    result = most_frequent_bomb(N, K, bombs)
    print(result)

if __name__ == "__main__":
    main()
