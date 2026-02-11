import sys
from functools import lru_cache

# REMOVE BEFORE SUBMIT
#sys.stdin = open("vpw2026/aardbei.invoer", "r")

@lru_cache(None)
def backtrack(path, choices, max, curw, minchoice):
    if curw + minchoice > max:
        yield path
    else:
        for i, w in enumerate(choices):
            if curw + w <= max:
                p = sorted(list(path)+[i])
                # prune choices
                yield from backtrack(tuple(p), choices, max, curw+w, minchoice)

# Read the number of lines
N = int(input())

for _ in range(N):
    line = input()  # remove trailing newline
    num_dishes, max_weight = list(map(int, line.split()))
    dishes = []
    for d in range(num_dishes):
        line = input()
        dish_weight, dish_sf, dish_delta = list(map(int, line.split()))
        dishes.append([dish_weight, dish_sf, dish_delta])

    #print(num_dishes, max_weight, dishes)

    benny_bennassi = []
    for dish in dishes:
        dishlist = [dish[1]]
        current_satisfaction = 0
        gained_satisfaction = dish[1]-dish[2]
        while gained_satisfaction > 0:
            dishlist.append(current_satisfaction + gained_satisfaction)
            gained_satisfaction -= dish[2]
        benny_bennassi.append(dishlist)
        
    #print(benny_bennassi)

    #determine_weight([], [d[0] for d in dishes], max_weight)
    winnaar = 0
    permset = set()
    for perm in backtrack(tuple(), tuple([d[0] for d in dishes]), max_weight, 0, min([d[0] for d in dishes])):
        t = sorted(perm)
        permset.add(tuple(t))
    #print("L",permset)

    for perm in permset:
        dishpointer = [0] * num_dishes
        total = 0
        #print(perm)
        for p in perm:
            if dishpointer[p] < len(benny_bennassi[p]):
                total += benny_bennassi[p][dishpointer[p]]
                dishpointer[p] += 1

        if total > winnaar:
            winnaar = total
        #print(perm)
    print(_+1,winnaar)


    

