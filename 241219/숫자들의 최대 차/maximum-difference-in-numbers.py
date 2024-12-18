def read_input():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    N, K = map(int, data[0].split())
    elements = list(map(int, data[1:]))
    return N, K, elements

def max_elements_within_range(N, K, elements):
    elements.sort()
    left, max_count = 0, 0

    for right in range(N):
        while elements[right] - elements[left] > K:
            left += 1
        max_count = max(max_count, right - left + 1)

    return max_count

def main():
    N, K, elements = read_input()
    result = max_elements_within_range(N, K, elements)
    print(result)

if __name__ == "__main__":
    main()
