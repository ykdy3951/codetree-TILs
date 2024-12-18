def read_input():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().strip().split()))
    return data

def find_abcd(values):
    values.sort()

    A = values[0]
    B = values[1]
    for C in values[2:]:
        D = values[-1] - A - B - C
        if D in values:
            return A, B, C, D

def main():
    values = read_input()
    A, B, C, D = find_abcd(values)
    print(A, B, C, D)

if __name__ == "__main__":
    main()
