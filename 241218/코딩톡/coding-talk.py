def read_input():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    n, m, p = map(int, data[0].split())
    messages = []
    for i in range(1, m + 1):
        sender, unread_count = data[i].split()
        messages.append((sender, int(unread_count)))
    return n, m, p, messages

def find_possible_unread_people(n, m, p, messages):
    people = [chr(ord('A') + i) for i in range(n)]
    s = set(people)

    if not messages[p-1][1]:
        return []

    for idx, (sender, unread_count) in enumerate(messages[p-1:]):
        if sender not in s:
            continue
        s.remove(sender)

    return sorted(list(s))

def main():
    n, m, p, messages = read_input()
    result = find_possible_unread_people(n, m, p, messages)
    print(" ".join(result))

if __name__ == "__main__":
    main()