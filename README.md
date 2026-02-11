# Mythical Man Moth @VPW

## Debugging Python Scripts with stdin in VS Code

When working on contest problems, your Python scripts usually read from **stdin** and write to **stdout**. To debug these scripts in VS Code while inspecting variables and stepping through code, you can use an **input file**.

---

### 1. Create a Test Input File

Create a file called `input.txt` in your project folder:

```
3
1 2 3
4 5 6
7 8 9
```

This file will simulate the contest input.

---

### 2. Redirect stdin in Your Script

At the top of your Python script, add:

``````python
import sys

# Redirect stdin to the file for debugging
sys.stdin = open("input.txt", "r")

# Read the number of lines
N = int(sys.stdin.readline())

# Process each line one by one
for _ in range(N):
    line = sys.stdin.readline().strip()  # remove trailing newline
    numbers = list(map(int, line.split()))  # convert space-separated numbers to integers
    print(numbers)  # example: print or process the line
```



```python
import sys

sys.stdin = open("input.txt", "r")  # redirect stdin to the input file

data = sys.stdin.read().split()
it = iter(data)

def ni(): return int(next(it))
def ns(): return next(it)
```

Now your code will read input from `input.txt` instead of waiting for manual input.

---

### 3. Configure VS Code Debugging

1. Open `.vscode/launch.json` (create it if it doesn’t exist).  
2. Add a configuration like this:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Debug with Input",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "args": [],
            "console": "integratedTerminal",
            "justMyCode": true,
            "redirectOutput": false
        }
    ]
}
```

3. Set breakpoints in your code wherever you want to inspect variables.  
4. Start debugging with the green "Run and Debug" button.

---

### 4. Tips for Debugging Contest Scripts

- **Hover over variables** to see their current values.  
- **Use the Debug Console** to evaluate expressions or modify variables.  
- **Conditional breakpoints**: stop only when a variable reaches a specific value (e.g., `i == 1000`).  
- **Step into/over** loops to follow algorithm execution.  

---

### 5. Ready-to-Use Template Example

```python
import sys

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
```

- Keep the `sys.stdin = open("input.txt", "r")` line **only for local debugging**.  
- Remove or comment it out when submitting code to the contest, as the judge will provide stdin automatically.




## Code Snippets Table of contents
- **Code snippets**
  - [Helper functions](#helper-functions)
    - [Snelle I/O voor wedstrijden](#snelle-io-voor-wedstrijden)
    - [Snelle input + automatische type‑conversie](#snelle-input--automatische-type-conversie)
    - [Combinaties & Permutaties (built-in)](#combinaties--permutaties-built-in)
    - [Bitmask‑subset iteratie](#bitmasksubset-iteratie)
    - [Recursie met memo (cache)](#recursie-met-memo-cache)
  - [Graphs](#graphs)
    - [DFS & BFS voor grafen](#dfs--bfs-voor-grafen)
    - [Dijkstra voor gewogen grafen](#dijkstra-voor-gewogen-grafen)
    - [Grid‑BFS + richtingenbord](#gridbfs--richtingenbord)
    - [Shortest path (BFS voor unweighted)](#shortest-path-bfs-voor-unweighted)
    - [Union‑Find (disjoint set)](#unionfind-disjoint-set)
    - [Topologische sort](#topologische-sort)
  - [Mathematical / Number theory](#mathematical--number-theory)
    - [Sieve van Eratosthenes (snelle priemtests)](#sieve-van-eratosthenes-snelle-priemtests)
    - [Nim‑winnende zetten (voorbeeld uit VPW 2017)](#nimwinnende-zetten-voorbeeld-uit-vpw-2017)
    - [Ontbrekend element in reeks (VPW 2017)](#ontbrekend-element-in-reeks-vpw-2017)
    - [Prime factorisatie (snelle trial)](#prime-factorisatie-snelle-trial)
  - [Dynamic Programming / Optimization](#dynamic-programming--optimization)
    - [Dynamische programmering — voorbeeld sub-string of knapsack](#dynamische-programmering--voorbeeld-sub-string-of-knapsack)
    - [Sliding window / two pointers](#sliding-window--two-pointers)
  - [Combinatorial](#combinatorial)
    - [Backtracking / Permutaties](#backtracking--permutaties)
  - [String manipulation / Other](#string-manipulation--other)
    - [Frequency count of characters in a string](#frequency-count-of-characters-in-a-string)
    - [Simple substring search (brute force)](#simple-substring-search-brute-force)
    - [KMP algorithm for substring search](#kmp-algorithm-for-substring-search)
    - [Reverse a string](#reverse-a-string)
    - [Check if string is palindrome](#check-if-string-is-palindrome)
    - [Binary search + bisect](#binary-search--bisect)
  - [Sorting](#sorting)
    - [Merge Sort](#merge-sort)
    - [Quick Sort](#quick-sort)
    - [Counting Sort (integers, onk)](#counting-sort-integers-onk)

## Code snippets

### Helper functions

#### 📌 Snelle I/O voor wedstrijden

Competitie-problemen hebben vaak veel inputdata — lees alles in één keer.

```python
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


```python
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


```python
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

```python
def subsets_mask(n):
    for mask in range(1<<n):
        yield [i for i in range(n) if mask & (1<<i)]
```

#### 📌 Recursie met memo (cache)

**Gebruik:** Vermijden van dubbele berekeningen in recursieve functies (Fibonacci, DP).  

**Wat gebeurt er:** `lru_cache` slaat eerdere resultaten op; functie rekent alleen nieuwe waarden uit.

```python
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

```python
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

```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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


```python
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

#### 📌 Backtracking / Permutaties

Handig bij puzzel-achtige opgaven (bijvoorbeeld sokoban-achtige puzzles).

**Gebruik:** Voor het genereren van alle mogelijke volgordes, combinaties of puzzeloplossingen zoals Sokoban of Sudoku.  

**Wat gebeurt er:** Recursief wordt elk element gekozen en toegevoegd aan het huidige pad; wanneer alle keuzes gebruikt zijn, wordt het pad “yielded”.


```python
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


## String manipulation / Other

#### 📌 Frequency count of characters in a string

```python
def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq
```

#### 📌 Simple substring search (brute force)

```python
def find_substring(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            return i
    return -1
```

#### 📌KMP algorithm for substring search

```python
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0]*len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j  # match found
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1
```

#### 📌Reverse a string

```python
def reverse_string(s):
    return s[::-1]
```

#### 📌Check if string is palindrome

```python
def is_palindrome(s):
    return s == s[::-1]
```

#### 📌 Binary search + bisect
**Gebruik:** Snel zoeken of invoegen in een gesorteerde array.  

**Wat gebeurt er:** `bisect_left` geeft positie terug waar een element kan worden toegevoegd zodat de array gesorteerd blijft.


```python
import bisect

arr = sorted([5,2,9])
pos = bisect.bisect_left(arr, 7) # positie om 7 in te voegen
```


## Sorting

#### 📌 Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
```

#### 📌 Quick Sort

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
```

#### 📌 Counting Sort (integers, O(n+k))

```python
def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    count = [0]*(max_val+1)
    for x in arr:
        count[x] += 1
    res = []
    for i, c in enumerate(count):
        res.extend([i]*c)
    return res
```
