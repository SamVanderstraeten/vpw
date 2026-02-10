# Mythical Man Moth @VPW

## TODO

- Feed all previous exercises to Chad
- Compile Top 20 list of most useful algorithms
- Debug application when running from terminal


## Code snippets

📌 1) Snelle I/O voor wedstrijden

Competitie-problemen hebben vaak veel inputdata — lees alles in één keer.

```
import sys

data = sys.stdin.read().strip().split()
# data bevat nu alle tokens van invoer
it = iter(data)

# voorbeeld als eerste token een getal N is
N = int(next(it))
for _ in range(N):
    x = int(next(it))
    # verwerk x
```

📌 2) Backtracking / Permutaties

Handig bij puzzel-achtige opgaven (bijvoorbeeld sokoban-achtige puzzles).

Gebruik:

Probleemtypen: alle mogelijke volgordes, combinaties of puzzels uitproberen, zoals Sokoban, sudoku, of kleine combinatorische zoekruimtes.

Handig als de zoekruimte relatief klein is, omdat het exponentieel kan worden.

Wat gebeurt er in de code:

path houdt de huidige gekozen elementen bij.

choices zijn de overgebleven opties om te kiezen.

Basisgeval: if not choices: → alle keuzes zijn gemaakt, yield het pad.

Anders: voor elk element c in choices, kies het, verwijder het uit de rest (choices[:i]+choices[i+1:]) en recursief verdergaan.

yield from zorgt dat alle gegenereerde permutaties worden doorgegeven

```
def backtrack(path, choices):
    if not choices:
        yield path
    else:
        for i, c in enumerate(choices):
            yield from backtrack(path + [c], choices[:i] + choices[i+1:])

# gebruik
for perm in backtrack([], [1,2,3]):
    print(perm)
```

Gebruik dit ook om combinaties of plaatsen van objecten uit te proberen.

📌 3) DFS & BFS voor grafen

Velden als mijnenveld, sokoban of kortste pad komen vaak voor.

```
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
```

📌 4) Dijkstra voor gewogen grafen

Als een opgave kortste paden met gewichten vraagt.

```
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
```

📌 5) Sieve van Eratosthenes (snelle priemtests)

Als je met primes moet werken.

```
def sieve(n):
    isprime = [True]*(n+1)
    isprime[0] = isprime[1] = False
    for i in range(2,int(n**0.5)+1):
        if isprime[i]:
            for j in range(i*i, n+1, i):
                isprime[j] = False
    return [i for i, p in enumerate(isprime) if p]
```

📌 6) Combinaties & Permutaties (built-in)

Handig als je geen handmatige backtrack wilt.

```
import itertools

for comb in itertools.combinations([1,2,3,4], 2):
    print(comb)

for perm in itertools.permutations([1,2,3]):
    print(perm)
```

📌 7) Dynamische programmering — voorbeeld sub-string of knapsack

Makkelijk aan te passen naar echte contest-vragen.

```
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
```

📌 8) Snelle input + automatische type‑conversie

Dit helpt bij veel testcases met grote data.

```
import sys

data = sys.stdin.buffer.read().split()
it = iter(data)

def ni(): return int(next(it))
def ns(): return next(it).decode()
```

Gebruik ni() en ns() voor snelle parsing zonder veel boilerplate.

📌 9) Grid‑BFS + richtingenbord

Nuttig voor labyrinth/grid‑problemen:

```
from collections import deque

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs_grid(start, grid):
    R, C = len(grid), len(grid[0])
    q = deque([start])
    dist = {start: 0}
    while q:
        r,c = q.popleft()
        for dr,dc in dirs:
            nr,nc = r+dr, c+dc
            if 0<=nr<R and 0<=nc<C and (nr,nc) not in dist and grid[nr][nc] != '#':
                dist[(nr,nc)] = dist[(r,c)] + 1
                q.append((nr,nc))
    return dist
```

📌 10) Nim‑winnende zetten (voorbeeld uit VPW 2017)

```
def winning_moves(piles):
    xor_val = 0
    for p in piles:
        xor_val ^= p
    moves = []
    for i,p in enumerate(piles):
        target = p ^ xor_val
        if target < p:
            new = piles.copy()
            new[i] = target
            moves.append(new)
    return sorted(moves)
```

📌 11) Ontbrekend element in reeks (VPW 2017)

```
def missing_number(arr):
    n = len(arr) + 1
    full_sum = n*(n+1)//2
    curr_sum = sum(arr)
    missing = full_sum - curr_sum
    return missing if 1 <= missing <= max(arr) else None
```

📌 12) Union‑Find (disjoint set)

Handig voor connectiviteitsproblemen:

```
class UF:
    def __init__(self,n):
        self.p = list(range(n))
    def find(self,x):
        if self.p[x]!=x:
            self.p[x]=self.find(self.p[x])
        return self.p[x]
    def union(self,x,y):
        rx,ry = self.find(x),self.find(y)
        if rx!=ry:
            self.p[ry]=rx
```

📌 13) Topologische sort

Als er een dependency‑graaf is:

```
from collections import deque

def topo_sort(n, adj):
    indeg = [0]*n
    for u in range(n):
        for v in adj[u]:
            indeg[v]+=1
    q = deque([i for i in range(n) if indeg[i]==0])
    res=[]
    while q:
        u=q.popleft()
        res.append(u)
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:
                q.append(v)
    return res
```

📌 14) Sliding window / two pointers

Voor array‑problemen met subranges:

```
def max_subarray_sum_at_most_k(arr, k):
    left=0
    curr=0
    best=0
    for right,x in enumerate(arr):
        curr+=x
        while curr>k:
            curr-=arr[left]
            left+=1
        best=max(best,curr)
    return best
```

📌 15) Binary search + bisect

```
import bisect

arr = sorted([5,2,9])
pos = bisect.bisect_left(arr, 7) # positie om 7 in te voegen
```


📌 16) Prime factorisatie (snelle trial)

```
def prime_factors(n):
    i=2
    res=[]
    while i*i <= n:
        while n%i==0:
            res.append(i)
            n//=i
        i+=1
    if n>1:
        res.append(n)
    return res
```

📌 17) Bitmask‑subset iteratie

Handig bij combinatorische problemen:

```
def subsets_mask(n):
    for mask in range(1<<n):
        yield [i for i in range(n) if mask & (1<<i)]
```

📌 18) Shortest path (BFS voor unweighted)

```
from collections import deque

def shortest_unweighted(adj, start):
    q = deque([start])
    dist = {start: 0}
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u]+1
                q.append(v)
    return dist
```

📌 19) Recursie met memo (cache)

```
from functools import lru_cache

@lru_cache(None)
def f(x):
    if x < 2:
        return x
    return f(x-1)+f(x-2)
```
