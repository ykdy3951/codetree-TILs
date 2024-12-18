def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    N = int(data[0])
    seats = list(map(int, data[1]))
    return N, seats

def max_distance_after_placement(N, seats):
    max_min_distance = 0

    for i in range(N):
        if seats[i] == 0:
            seats[i] = 1
            min_distance = float('inf')
            last_person = -1

            for j in range(N):
                if seats[j] == 1:
                    if last_person != -1:
                        min_distance = min(min_distance, (j - last_person) // 2)
                    last_person = j

            max_min_distance = max(max_min_distance, min_distance)
            seats[i] = 0

    return max_min_distance

def main():
    N, seats = read_input()
    result = max_distance_after_placement(N, seats)
    print(result+1)

if __name__ == "__main__":
    main()
