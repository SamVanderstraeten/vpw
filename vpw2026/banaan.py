import sys

# REMOVE BEFORE SUBMIT
#sys.stdin = open("vpw2026/hindex.invoer", "r")

# Read the number of lines
N = int(input())

t = {}
for _ in range(N):
    line = input()  # remove trailing newline
    numbers = list(map(int, line.split()))
    
    for i in range(len(numbers), 0, -1):
        if len([x for x in numbers if x >= i]) >= i:
            print(_+1,i)
            break