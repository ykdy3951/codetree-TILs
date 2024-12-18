def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    N = int(data[0])
    seats = list(map(int, data[1]))
    return N, seats

def max_distance_after_placement(N, seats):
    def calculate_min_distance(seats):
        min_dist = float('inf')
        last_filled = -1

        for i in range(N):
            if seats[i] == 1:
                if last_filled != -1:
                    min_dist = min(min_dist, (i - last_filled))
                last_filled = i
        return min_dist if min_dist != float('inf') else 0

    max_distance = 0

    for i in range(N):
        if seats[i] == 0:
            seats[i] = 1
            current_min_distance = calculate_min_distance(seats)
            max_distance = max(max_distance, current_min_distance)
            seats[i] = 0

    return max_distance


def main():
    N, seats = read_input()
    result = max_distance_after_placement(N, seats)
    print(result)

if __name__ == "__main__":
    main()
