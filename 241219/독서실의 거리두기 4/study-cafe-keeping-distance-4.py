def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    N = int(data[0])
    seats = list(map(int, data[1]))
    return N, seats

def max_distance_two_people(N, seats):
    def calculate_min_distance(seats):
        min_dist = float('inf')
        last_filled = -1

        for i in range(N):
            if seats[i] == 1:
                if last_filled != -1:
                    min_dist = min(min_dist, i - last_filled)
                last_filled = i

        return min_dist

    max_min_distance = 0

    for i in range(N):
        if seats[i] == 0:
            seats[i] = 1
            for j in range(i + 1, N):
                if seats[j] == 0:
                    seats[j] = 1
                    current_min_distance = calculate_min_distance(seats)
                    max_min_distance = max(max_min_distance, current_min_distance)
                    seats[j] = 0
            seats[i] = 0

    return max_min_distance

def main():
    N, seats = read_input()
    result = max_distance_two_people(N, seats)
    print(result)

if __name__ == "__main__":
    main()
