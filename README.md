# Mythical Man Moth @VPW

## TODO

- Feed all previous exercises to Chad
- Compile Top 20 list of most useful algorithms
- Debug application when running from terminal


## Code snippets

### Helper functions

#### 📌 Snelle I/O voor wedstrijden

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


#### 📌 Snelle input + automatische type‑conversie

Dit helpt bij veel testcases met grote data.

**Gebruik:** Voor snelle parsing van grote inputdata bij veel testcases.  

**Wat gebeurt er:** Alle input wordt ingelezen als bytes, opgesplitst, en door een iterator gehaald; `ni()` en `ns()` geven respectievelijk int of string.


```
import sys

data = sys.stdin.buffer.read().split()
it = iter(data)

def ni(): return int(next(it))
def ns(): return next(it).decode()
```

Gebruik ni() en ns() voor snelle parsing zonder veel boilerplate.

#### 📌 Combinaties & Permutaties (built-in)

Handig als je geen handmatige backtrack wilt.

**Gebruik:** Snel alle combinaties of permutaties genereren zonder handmatige backtracking.  

**Wat gebeurt er:** `itertools.combinations` genereert subsets van vaste grootte; `itertools.permutations` genereert alle volgordes.


```
import itertools

for comb in itertools.combinations([1,2,3,4], 2):
    print(comb)

for perm in itertools.permutations([1,2,3]):
    print(perm)
```

#### 📌 Bitmask‑subset iteratie

**Gebruik:** Alle subsets genereren van een set, handig voor combinatorische problemen.  

**Wat gebeurt er:** Loop over alle mogelijke bitmasks; elk mask representeert een subset van indices waar de bit 1 staat.


Handig bij combinatorische problemen:

```
def subsets_mask(n):
    for mask in range(1<<n):
        yield [i for i in range(n) if mask & (1<<i)]
```

#### 📌 Recursie met memo (cache)

**Gebruik:** Vermijden van dubbele berekeningen in recursieve functies (Fibonacci, DP).  

**Wat gebeurt er:** `lru_cache` slaat eerdere resultaten op; functie rekent alleen nieuwe waarden uit.

```
from functools import lru_cache

@lru_cache(None)
def f(x):
    if x < 2:
        return x
    return f(x-1)+f(x-2)
```


### Graphs

#### 📌 DFS & BFS voor grafen

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

#### 📌 Dijkstra voor gewogen grafen

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

#### 📌 9) Grid‑BFS + richtingenbord

Nuttig voor labyrinth/grid‑problemen:

**Gebruik:** Kortste pad of bereikbaarheid in een grid of labyrinth.  

**Wat gebeurt er:** BFS loopt over de grid, houdt afstand bij in een dictionary en negeert muren of reeds bezochte cellen.


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



#### 📌 Shortest path (BFS voor unweighted)

**Gebruik:** Kortste pad in een ongewogen graf.  

**Wat gebeurt er:** BFS houdt afstand bij vanaf startknoop; elke nieuwe knoop wordt toegevoegd met afstand +1.


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

#### 📌 Union‑Find (disjoint set)

Handig voor connectiviteitsproblemen:
**Gebruik:** Connectiviteitsproblemen, componentdetectie of cyclusdetectie in grafen.  
**Wat gebeurt er:** `find` zoekt de root van een element (met path compression), `union` verbindt twee sets.


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

#### 📌 Topologische sort

Als er een dependency‑graaf is:
**Gebruik:** Taken met afhankelijkheden, zoals projecten of opdrachten.  
**Wat gebeurt er:** BFS-achtige methode die knopen met indegree 0 in volgorde verwerkt; levert een topologische volgorde voor een DAG.


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

### Mathematical / Number theory

#### 📌 Sieve van Eratosthenes (snelle priemtests)

Als je met primes moet werken.
**Gebruik:** Snel alle priemgetallen ≤ n vinden.  
**Wat gebeurt er:** Een lijst houdt bij welke getallen prime zijn; veelvouden van elke prime worden uitgesloten.


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



#### 📌 Nim‑winnende zetten (voorbeeld uit VPW 2017)

**Gebruik:** Speltheorie – alle zetten vinden die naar een winnende positie leiden.  
**Wat gebeurt er:** Nim-sum wordt berekend, en voor elke stapel wordt gecontroleerd of aanpassen leidt tot een winnende configuratie.


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

#### 📌 Ontbrekend element in reeks (VPW 2017)

**Gebruik:** Vind het ontbrekende getal in een rij 1..n.  
**Wat gebeurt er:** Som van 1..n berekend en verschil genomen met huidige som om het ontbrekende element te vinden.


```
def missing_number(arr):
    n = len(arr) + 1
    full_sum = n*(n+1)//2
    curr_sum = sum(arr)
    missing = full_sum - curr_sum
    return missing if 1 <= missing <= max(arr) else None
```

#### 📌 Prime factorisatie (snelle trial)

**Gebruik:** Alle priemfactoren van een getal vinden.  
**Wat gebeurt er:** Iteratief delen door priemgetallen; elke factor wordt toegevoegd aan de lijst; eventuele resterende n > 1 is ook een factor.


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

## Dynamic Programming / Optimization

#### 📌 Dynamische programmering — voorbeeld sub-string of knapsack

Makkelijk aan te passen naar echte contest-vragen.
**Gebruik:** Optimalisatieproblemen zoals knapsack, substrings of subsequences.  
**Wat gebeurt er:** `dp[i][j]` houdt de maximale waarde bij voor de eerste i items en capaciteit j; voor elk item wordt gekeken of opnemen beter is dan niet opnemen.


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


#### 📌 Sliding window / two pointers

Voor array‑problemen met subranges:
**Gebruik:** Problemen met subarrays, limieten of maximale sommen.  
**Wat gebeurt er:** Twee pointers schuiven over array; houd de som bij en pas aan wanneer limiet overschreden wordt.


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


### Combinatorial

#### 📌 2) Backtracking / Permutaties

Handig bij puzzel-achtige opgaven (bijvoorbeeld sokoban-achtige puzzles).

**Gebruik:** Voor het genereren van alle mogelijke volgordes, combinaties of puzzeloplossingen zoals Sokoban of Sudoku.  

**Wat gebeurt er:** Recursief wordt elk element gekozen en toegevoegd aan het huidige pad; wanneer alle keuzes gebruikt zijn, wordt het pad “yielded”.


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
