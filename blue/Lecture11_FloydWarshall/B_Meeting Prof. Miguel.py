def convertCapitalLetterToNumber(c):
    return ord(c) - 65


def FloydWarshall(dist, n):
    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


def addSet(set, val):
    consistVal = False
    idx = -1
    for i in range(len(set)):
        if set[i] == val:
            consistVal = True
            break
    if consistVal == False:
        set.append(val)
        idx = len(set) - 1
    return idx

def zerofyGraph(n, graph):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0

INF = 10**9
M = -1
while M != 0:
    M = int(input())
    if M != 0:
        set = []
        index_val_map = [-1 for _ in range(127)]
        val_index_map = [-1 for _ in range(127)]
        inp = []
        for _ in range(M):
            arr = list(input().split())
            w = int(arr[4])
            u = ord(arr[2])
            v = ord(arr[3])

            # idx_u and idx_v are index of corresponding nodes in graph
            idx_u = addSet(set, u)
            idx_v = addSet(set, v)

            if idx_u != -1:
                index_val_map[idx_u] = u
                val_index_map[u] = idx_u
            if idx_v != -1:
                index_val_map[idx_v] = v
                val_index_map[v] = idx_v

            inp.append((arr[0], val_index_map[u], val_index_map[v], w))
            if arr[1] == 'B':
                inp.append((arr[0], val_index_map[v], val_index_map[u], w))

        posYoung, posMedium = input().split()
        if posYoung == posMedium:
            print(0, posYoung)
        else:
            N = len(set)
            distY = [[INF for _ in range(N)] for _ in range(N)]
            zerofyGraph(N, distY)
            distM = [[INF for _ in range(N)] for _ in range(N)]
            zerofyGraph(N, distM)

            for obj in inp:
                age_type = obj[0]
                a = obj[1]
                b = obj[2]
                weight = obj[3]
                if age_type == 'Y':
                    if distY[a][b] > weight:
                        distY[a][b] = weight
                if age_type == 'M':
                    if distM[a][b] > weight:
                        distM[a][b] = weight

            FloydWarshall(distY, N)
            FloydWarshall(distM, N)

            ans_dist = INF
            ans_point = -1
            posY = val_index_map[ord(posYoung)]
            posM = val_index_map[ord(posMedium)]
            if posY == -1 or posM == -1:
                print('You will never meet.')
            else:
                for i in range(N):
                    if True:
                        from_Y_to_this_point = distY[posY][i]
                        from_M_to_this_point = distM[posM][i]
                        total_dist = from_Y_to_this_point + from_M_to_this_point
                        if total_dist < ans_dist:
                            ans_dist = total_dist
                            ans_point = i
                if ans_dist != INF:
                    print(ans_dist, chr(index_val_map[ans_point]))
                else:
                    print('You will never meet.')
