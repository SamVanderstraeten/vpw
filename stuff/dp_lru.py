'''
Find the maximum value that can be put in a knapsack of capacity W given n items with values and weights.
This is a classic problem that can be solved using Dynamic Programming (DP).
Key Points:
1. Recursive Structure: The problem can be broken down into smaller subproblems, which is ideal for a recursive approach.
2. Overlapping Subproblems: The same subproblems are solved multiple times, making it a perfect candidate for memoization.
3. Optimal Substructure: The optimal solution can be constructed from optimal solutions of its subproblems.
Python's @lru_cache decorator from the functools module provides an easy way to implement memoization, which can significantly reduce the time complexity from exponential to polynomial.
'''

import sys
from functools import lru_cache

# 1. Increase recursion depth for deep DP trees
sys.setrecursionlimit(2000)

def solve():
    # Example Data: (Value, Weight)
    # Often provided as two separate lists in problems
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    n = len(values)

    # 2. Define the recursive function with the cache decorator
    # maxsize=None ensures it acts as a full memoization table
    @lru_cache(maxsize=None)
    def knapsack(index, remaining_capacity):
        # Base Case: No more items or no more room in the bag
        if index == n or remaining_capacity <= 0:
            return 0
        
        # Choice 1: Skip the current item
        # We move to the next index but the capacity stays the same
        res = knapsack(index + 1, remaining_capacity)
        
        # Choice 2: Take the current item (if it fits)
        if weights[index] <= remaining_capacity:
            # Value of current item + best value from remaining capacity
            take_item = values[index] + knapsack(index + 1, remaining_capacity - weights[index])
            res = max(res, take_item)
            
        return res

    # 3. Call the function starting at the first item
    print(f"Maximum Value: {knapsack(0, capacity)}")

if __name__ == "__main__":
    solve()