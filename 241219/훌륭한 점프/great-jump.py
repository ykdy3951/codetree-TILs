def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    n, k = map(int, data[0].split())
    stones = list(map(int, data[1].split()))
    return n, k, stones

def min_max_of_path(n, k, stones):
    dp = [float('inf')] * n
    dp[0] = stones[0]

    for i in range(1, n):
        for j in range(max(0, i - k), i):
            dp[i] = min(dp[i], max(dp[j], stones[i]))

    return dp[-1]

def main():
    n, k, stones = read_input()
    result = min_max_of_path(n, k, stones)
    print(result)

if __name__ == "__main__":
    main()
