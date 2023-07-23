import queue

while True: #I want That loop is terminated when getting EOF
    try:
        n = int(input())
        s = []
        q = queue.Queue()
        S, Q, PQ = 1, 1, 1
        pq = queue.PriorityQueue()
        for _ in range(n):
            type, val = map(int, input().split())
            if type == 1:
                s.append(val)
                q.put(val)
                pq.put(-val) # maxPQ
            else:
                popped_s = s.pop()
                popped_q = q.get()
                popped_pq = -pq.get()
                if popped_s != val:
                    S = 0
                if popped_q != val:
                    Q = 0
                if popped_pq != val:
                    PQ = 0
        if S + Q + PQ == 0:
            print('impossible')
        elif S + Q + PQ > 1:
            print('not sure')
        else:
            if S == 1:
                print('stack')
            if Q == 1:
                print('queue')
            if PQ == 1:
                print('priority queue')
    except EOFError:
        break
