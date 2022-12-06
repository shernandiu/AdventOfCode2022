from collections import deque


def foo(text: str, goal: int):
    # unique_chars = dict
    substring = deque(text[:goal])
    print(substring)
    for i, char in enumerate(text[goal:]):
        if len(set(substring)) == goal:
            return i+goal
        substring.append(char)
        substring.popleft()


with open('input/day6.sql', 'r') as f:
    text = f.read().strip()
    print(foo(text, 4))
    print(foo(text, 14))
