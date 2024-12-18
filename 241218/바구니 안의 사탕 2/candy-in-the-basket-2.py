def read_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N, K = map(int, data[0].split())
    baskets = []
    for i in range(1, N + 1):
        candies, position = map(int, data[i].split())
        baskets.append((position, candies))
    return N, K, baskets

def max_candies(N, K, baskets):
    max_candies_count = 0

    for c in range(101):
        current_candies = 0
        for position, candies in baskets:
            if c - K <= position <= c + K:
                current_candies += candies
        max_candies_count = max(max_candies_count, current_candies)

    return max_candies_count

def main():
    N, K, baskets = read_input()
    result = max_candies(N, K, baskets)
    print(result)

if __name__ == "__main__":
    main()
