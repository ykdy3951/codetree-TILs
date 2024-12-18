def read_input():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().strip().split()))
    return data

def min_difference_between_teams(abilities):
    from itertools import combinations
    total_sum = sum(abilities)
    min_difference = float('inf')

    for team1 in combinations(abilities, 3):
        team1_sum = sum(team1)
        team2_sum = total_sum - team1_sum
        difference = abs(team1_sum - team2_sum)
        min_difference = min(min_difference, difference)

    return min_difference

def main():
    abilities = read_input()
    result = min_difference_between_teams(abilities)
    print(result)

if __name__ == "__main__":
    main()
