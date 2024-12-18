def read_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N, H, T = map(int, data[0].split())
    heights = list(map(int, data[1].split()))
    return N, H, T, heights

def min_cost_to_make_uniform(N, H, T, heights):
    min_cost = float('inf')

    for i in range(N - T + 1):
        current_cost = 0
        for j in range(i, i + T):
            current_cost += abs(heights[j] - H)
        min_cost = min(min_cost, current_cost)

    return min_cost

def main():
    N, H, T, heights = read_input()
    result = min_cost_to_make_uniform(N, H, T, heights)
    print(result)

if __name__ == "__main__":
    main()