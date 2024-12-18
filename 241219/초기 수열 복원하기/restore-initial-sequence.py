def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    N = int(data[0])
    sums = list(map(int, data[1].split()))
    return N, sums

def backtrack(sequence, used, index, N, sums):
    if index == N:
        # Check if all sums are correct
        for i in range(N - 1):
            if sequence[i] + sequence[i + 1] != sums[i]:
                return False
        return True

    for num in range(1, N + 1):
        if num not in used:
            sequence[index] = num
            used.add(num)

            if index == 0 or sequence[index - 1] + sequence[index] == sums[index - 1]:
                if backtrack(sequence, used, index + 1, N, sums):
                    return True

            used.remove(num)

    return False

def restore_sequence(N, sums):
    sequence = [0] * N
    used = set()

    if backtrack(sequence, used, 0, N, sums):
        return sequence
        
def main():
    N, sums = read_input()
    result = restore_sequence(N, sums)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
