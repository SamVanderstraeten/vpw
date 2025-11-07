"""
Schrijf een programma dat bepaalt hoeveel verschillende polyominos er zijn voor een gegeven N. 
Twee polyominos zijn verschillend indien ze niet door een draaiing van 90 of 180 graden in elkaar kunnen getransformeerd worden.

De invoer is een geheel getal N in [1,10], dus inclusief 1 en 10. De output is een geheel getal.
Voorbeeld:
N=2 -> 1 (domino)
N=4 -> 7 (tetris)
"""


# BRUTE FORCE would be (won't work, too much calcy-calcy)
# Create a grid of NxN 0s (so all possible combinations certainly fit)
# Create all possible configurations (set 1 for square)
# Check all generated configs for doubles
    # Minimize (delete all completely empty rows and cols)
    # Check complete overlaps with all rotations
# Count remaining
# Will take forever on N=10


# Soooooo.... Recursion time!
import copy

def printgrid(gridje):  
    for r in gridje:
        for k in r:
            print(k, end=" ")
        print()

# >> RECURSION FTW
def progress(form, current_x, current_y, num, stop):
    if num == stop:
        return [form]
    
    collection = []
    formcopy = copy.deepcopy(form)
    formcopy[current_x+1][current_y] = 1
    collection.extend(progress(formcopy, current_x+1, current_y, num+1, stop))
    
    formcopy2 = copy.deepcopy(form)
    formcopy2[current_x][current_y+1] = 1
    collection.extend(progress(formcopy2, current_x, current_y+1, num+1, stop))

    return collection


n = int(input())
grid = [[0]*n for _ in range(n)]
grid[0][0] = 1 # starting point
collection = progress(grid, 0, 0, 1, n)

"""for g in collection:
    printgrid(g)
    print("################")"""

print(len(collection)-1)
