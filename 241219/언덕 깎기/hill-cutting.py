def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    N = int(data[0])
    hills = list(map(int, data[1:]))
    return N, hills

def calculate_minimum_cost(N, hills):
    min_cost = float('inf')

    for low in range(0, 84):
        high = low + 17
        cost = 0

        for h in hills:
            if h < low:
                cost += (low - h) ** 2
            elif h > high:
                cost += (h - high) ** 2

        min_cost = min(min_cost, cost)

    return min_cost

def main():
    N, hills = read_input()
    result = calculate_minimum_cost(N, hills)
    print(result)

if __name__ == "__main__":
    main()
