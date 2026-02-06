def dijkstra_time(graph, start, end):
    return 0

def endpoint_check(graph, current, end, visited=[], total_cost=0):
    if graph[current][end] < float('inf'):
        return True # return total cost
    
    reachable = [x for x in range(len(graph[current])) if graph[current][x] < float('inf') and not x in visited]
    
    visited.append(current)
    for i in range(len(reachable)):
        result = endpoint_check(graph, reachable[i], end, visited, total_cost+graph[current][reachable[i]])
        if result == True:
            return True
    return float('inf')

aantal_tests = int(input())
for i in range(aantal_tests):
    print(str(i+1), end=" ")
    # Read graph
    num_nodes, num_edges = [int(x) for x in input().split(" ")]
    graph = [[float('inf')]*(num_nodes+1) for j in range(num_nodes+1)]
    for j in range(num_nodes+1):
        graph[j][j] = 0

    for e in range(num_edges):
        a,b,cost =  [int(x) for x in input().split(" ")]
        graph[a][b] = cost

    for k in range(num_nodes+1):
        for l in range(num_nodes+1):
            for m in range(num_nodes+1):
                if graph[l][m] > graph[l][k] + graph[k][m]:
                    graph[l][m] = graph[l][k] + graph[k][m]
    
    shortest = graph[1][num_nodes]

    loopy = False
    for j in range(num_nodes+1):
        if graph[j][j] < 0 and graph[1][j] != float('inf'):
            loopy = True

    if loopy:
        print("min oneindig")
    elif shortest == float('inf'):
        print("plus oneindig")
    else: 
        print(shortest)