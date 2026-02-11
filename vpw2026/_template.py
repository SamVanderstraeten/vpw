import sys

# REMOVE BEFORE SUBMIT
sys.stdin = open("input.txt", "r")

# Read the number of lines
N = int(input())

for _ in range(N):
    line = input()  # remove trailing newline
    numbers = list(map(int, line.split()))