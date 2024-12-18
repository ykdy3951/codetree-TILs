from itertools import permutations

def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    abilities = list(map(int, data))
    return abilities

def min_team_difference(abilities):
    min_diff = float('inf')
    valid = False

    for perm in permutations(abilities):
        team1 = perm[0] + perm[1]
        team2 = perm[2] + perm[3]
        team3 = perm[4]

        if len({team1, team2, team3}) == 3:
            valid = True
            max_team = max(team1, team2, team3)
            min_team = min(team1, team2, team3)
            min_diff = min(min_diff, max_team - min_team)

    return min_diff if valid else -1

def main():
    abilities = read_input()
    result = min_team_difference(abilities)
    print(result)

if __name__ == "__main__":
    main()