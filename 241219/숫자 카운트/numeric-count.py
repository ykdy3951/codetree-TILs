def read_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    N = int(data[0])
    queries = []
    for i in range(1, N + 1):
        parts = data[i].split()
        number = list(map(int, parts[0]))
        count1, count2 = map(int, parts[1:])
        queries.append((number, count1, count2))
    return N, queries

def calculate_counts(guess, number):
    count1 = sum(g == n for g, n in zip(guess, number))
    count2 = sum((g in number) and (g != number[i]) for i, g in enumerate(guess))
    return count1, count2

def count_possible_numbers(N, queries):
    possible_numbers = 0

    for a in range(1, 10):
        for b in range(1, 10):
            if a == b:
                continue
            for c in range(1, 10):
                if c == a or c == b:
                    continue
                guess = [a, b, c]
                valid = True
                for number, count1, count2 in queries:
                    calculated_count1, calculated_count2 = calculate_counts(guess, number)
                    if calculated_count1 != count1 or calculated_count2 != count2:
                        valid = False
                        break
                if valid:
                    possible_numbers += 1

    return possible_numbers

def main():
    N, queries = read_input()
    result = count_possible_numbers(N, queries)
    print(result)

if __name__ == "__main__":
    main()
