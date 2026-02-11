import sys


# VRFIX LAST MINUTE

# Redirect stdin to the file for debugging
sys.stdin = open("input.txt", "r")

# Read the number of lines
N = int(input())

# Process each line one by one
for _ in range(N):
    line = input()  # remove trailing newline
    numbers = list(map(int, line.split()))  # convert space-separated numbers to integers
    print(numbers)  # example: print or process the line

# / VRFIX LAST MINUTE


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

# SET STUFF
s = {1,2,3,4}
t = set([2,3,4,8,9,5])
0
s.add(18)
print(s)
print(s & t)

# MAX FROM DICT
l = {'a': 3, 'b': 400, 'c': 57}
print(max(l)) # 'c' (max key)
print(max(l, key=l.get)) # 'b' (max val)