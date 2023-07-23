import queue

def command(q, cmd):
    if cmd[0] == 'N':
        v = q.get()
        q.put(v)
        return q, v
    if cmd[0] == 'E':
        ord = int(cmd[1])
        q1 = queue.Queue()
        q1.put(ord)
        while q.empty() == False:
            v = q.get()
            if v != ord:
                q1.put(v)
        q = q1
        return q, ord

P = -1
tc = 1
while P != 0:
    P, C = map(int, input().split())
    if P != 0:
        print(f'Case {tc}: ')
        q = queue.Queue()
        for i in range(1, min(C+1,P+1)):
            q.put(i)
        while C > 0:
            cmd = list(input().split())
            q, v = command(q, cmd)
            if cmd[0] == 'N':
                print(v)
            C -= 1
        tc += 1