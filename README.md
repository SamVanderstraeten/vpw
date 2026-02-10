# Mythical Man Moth @VPW

## TODO

- Feed all previous exercises to Chad
- Compile Top 20 list of most useful algorithms
- Debug application when running from terminal


📌 1) Snelle I/O voor wedstrijden

Competitie-problemen hebben vaak veel inputdata — lees alles in één keer.

'''
import sys

data = sys.stdin.read().strip().split()
# data bevat nu alle tokens van invoer
it = iter(data)

# voorbeeld als eerste token een getal N is
N = int(next(it))
for _ in range(N):
    x = int(next(it))
    # verwerk x
'''

📌 2) Backtracking / Permutaties

Handig bij puzzel-achtige opgaven (bijvoorbeeld sokoban-achtige puzzles).

'''
def backtrack(path, choices):
    if not choices:
        yield path
    else:
        for i, c in enumerate(choices):
            yield from backtrack(path + [c], choices[:i] + choices[i+1:])

# gebruik
for perm in backtrack([], [1,2,3]):
    print(perm)
'''

Gebruik dit ook om combinaties of plaatsen van objecten uit te proberen.

📌 3) DFS & BFS voor grafen

Velden als mijnenveld, sokoban of kortste pad komen vaak voor.

'''
from collections import deque

# BFS voorbeeld (kortste pad op een grid of graf)
def bfs(start, neighbors):
    visited = {start}
    q = deque([start])
    while q:
        node = q.popleft()
        for nxt in neighbors(node):
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return visited

# DFS recursief
def dfs(node, neighbors, visited=None):
    if visited is None: visited = set()
    visited.add(node)
    for nxt in neighbors(node):
        if nxt not in visited:
            dfs(nxt, neighbors, visited)
    return visited
'''

📌 4) Dijkstra voor gewogen grafen

Als een opgave kortste paden met gewichten vraagt.

'''
import heapq

def dijkstra(adj, start):
    dist = {start: 0}
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in adj[u]:
            nd = d + w
            if v not in dist or nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
'''

📌 5) Sieve van Eratosthenes (snelle priemtests)

Als je met primes moet werken.

'''
def sieve(n):
    isprime = [True]*(n+1)
    isprime[0] = isprime[1] = False
    for i in range(2,int(n**0.5)+1):
        if isprime[i]:
            for j in range(i*i, n+1, i):
                isprime[j] = False
    return [i for i, p in enumerate(isprime) if p]
'''

📌 6) Combinaties & Permutaties (built-in)

Handig als je geen handmatige backtrack wilt.

'''
import itertools

for comb in itertools.combinations([1,2,3,4], 2):
    print(comb)

for perm in itertools.permutations([1,2,3]):
    print(perm)
'''

📌 7) Dynamische programmering — voorbeeld sub-string of knapsack

Makkelijk aan te passen naar echte contest-vragen.

'''
# klassieke knapsack (waarden en gewichten)
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1,n+1):
        w, v = weights[i-1], values[i-1]
        for j in range(W+1):
            dp[i][j] = dp[i-1][j]
            if j >= w:
                dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)
    return dp[n][W]
'''
