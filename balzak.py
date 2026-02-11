import sys

# Redirect stdin for debugging
sys.stdin = open("input.txt", "r")

# Fast input parsing
data = sys.stdin.read().split()
it = iter(data)
def ni(): return int(next(it))
def ns(): return next(it)

# Example usage
T = ni()
for _ in range(T):
    x = ni()
    print(x)