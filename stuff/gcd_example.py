'''
The Problem: "Distributing Goodies"
You have two types of snacks: 
$A$ chocolates and $B$ candies. 
You want to create identical gift bags such that:
- Every bag has the exact same number of chocolates.
- Every bag has the exact same number of candies.
- There are no leftover snacks.
What is the maximum number of identical bags you can create?

The Logic
The number of bags must be a divisor of $A$ (so chocolates can be split evenly) and a divisor of $B$ (so candies can be split evenly). 
To maximize the bags, we need the Greatest Common Divisor.

Python Solution
In a contest, don't reinvent the wheel. Use the built-in math.gcd function, which uses the efficient Euclidean Algorithm ($O(\log(\min(A, B)))$).
'''

import math

def solve():
    # Example inputs
    chocolates = 48
    candies = 72
    
    # The maximum number of bags is the GCD of both counts
    max_bags = math.gcd(chocolates, candies)
    
    print(f"Maximum bags possible: {max_bags}")
    print(f"Each bag will have {chocolates // max_bags} chocolates")
    print(f"Each bag will have {candies // max_bags} candies")

solve()

'''
Pro-Tip: 
The LCM Relationship
Often, problems ask about things "synching up" (e.g., two lights flashing at different intervals). 
For that, you need the Least Common Multiple (LCM).
The relationship between GCD and LCM is:$$\text{lcm}(a, b) = \frac{|a \cdot b|}{\text{gcd}(a, b)}$$

In Python 3.9+, you can just use math.lcm(a, b) directly.
'''


'''
When you need the GCD of more than two numbers—say an entire array—you use the Associative Property: $\text{gcd}(a, b, c) = \text{gcd}(a, \text{gcd}(b, c))$.In a programming contest, you'll usually see this when finding the largest possible "step size" that can reach all points on a grid or divide all resource piles.The Problem: "The Harmonious Array"You are given an array of integers. You want to find the largest integer $D$ that divides every single element in the array.Python ImplementationPython’s math.gcd is actually very powerful; since version 3.9, it can take multiple arguments or an entire unpacked list.Pythonimport math

def solve_array_gcd():
    # Example: A set of numbers like 24, 60, 84, 108
    nums = [24, 60, 84, 108]
    
    # Method 1: Python 3.9+ (Modern/Standard Contest Way)
    # The * operator unpacks the list into arguments
    result = math.gcd(*nums)
    
    print(f"The GCD of the array {nums} is: {result}")

    # Method 2: The "Old School" way (using a loop/reduce)
    # Useful to know if you are stuck on an older version or using a different language
    from functools import reduce
    result_manual = reduce(math.gcd, nums)
    
    print(f"Manual reduction result: {result_manual}")

solve_array_gcd()
A Common Variation: 
GCD with "Offsets"Sometimes the problem isn't just gcd(array). 
A popular contest trick is:"What is the largest $D$ such that all elements $A_i$ leave the same remainder when divided by $D$?"

The Trick: 
If $A_i \equiv r \pmod D$ and $A_j \equiv r \pmod D$, then $D$ must divide the difference $(A_i - A_j)$.
To solve this, you calculate the GCD of the differences between adjacent elements:$$\text{result} = \text{gcd}(A_1 - A_0, A_2 - A_1, \dots, A_n - A_{n-1})$$
'''