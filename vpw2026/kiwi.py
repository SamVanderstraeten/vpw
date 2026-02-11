import sys

# REMOVE BEFORE SUBMIT
sys.stdin = open("vpw2026/hutten.invoer", "r")

# Read the number of lines
N = int(input())

for _ in range(N):
    num_huts = int(input())

    hutlist = []
    for h in range(num_huts):
        line = input()
        hutlist.append(list(map(int, line.split())))

    matrix = [[float('inf')]*(num_huts) for j in range(num_huts)]
    for h1, hut1 in enumerate(hutlist):
        for h2, hut2 in enumerate(hutlist):
            if h1 == h2:
                continue
            dist = (hut1[0]-hut2[0])**2 + (hut1[1]-hut2[1])**2
            matrix[h1][h2] = dist
            matrix[h2][h1] = dist

    #print(matrix)

    connectionmap = [0]*num_huts
    #print(connectionmap)
    sum = 0
    while min(connectionmap) < 2:
        m = min([min(x) for x in matrix])
        for r, row in enumerate(matrix):
            if m in row:
                m_index = row.index(m)
                if m_index >= 0:
                    #print(connectionmap)
                    if connectionmap[r] < 2 and connectionmap[m_index] < 2:
                        sum += m
                        matrix[r][m_index] = float('inf')
                        matrix[m_index][r] = float('inf')
                        connectionmap[r] += 1
                        connectionmap[m_index] += 1

                        if connectionmap[r] == 2:
                            matrix[r] = [float('inf')] * num_huts
                        if connectionmap[m_index] == 2:
                            matrix[m_index] = [float('inf')] * num_huts
                        break
                    else:
                        matrix[r][m_index] = float('inf')
                        matrix[m_index][r] = float('inf')



    print(_+1,sum)             



    # sum = 0
    # for r in range(2):
    #     for i in range(len(matrix)):
    #         m = min(matrix[i])
    #         if m != float('inf'):
    #             m_index = matrix[i].index(m)
    #             sum += m
    #             matrix[i][m_index] = float('inf')
    #             matrix[m_index][i] = float('inf')

        # m = min(matrix[i])
        # if m != float('inf'):
        #     m_index = matrix[i].index(m)
        #     sum += m
        #     matrix[i][m_index] = float('inf')
        #     matrix[m_index][i] = float('inf')

    
    