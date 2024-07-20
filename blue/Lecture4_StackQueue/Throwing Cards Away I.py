import queue

def solve(n):
    q = queue.Queue()
    discarded_cards = []
    for i in range(1, n+1):
        q.put(i)
    i = 0
    while q.qsize() > 1:
        if i % 2 == 0:
            discarded_cards.append(q.get())
        else:
            q.put(q.get())
        i += 1
    if len(discarded_cards) != 0:
        print('Discarded cards: ', end='')
        print(*discarded_cards, sep=', ')
    else:
        print('Discarded cards:', end='')
        print()
    print('Remaining card:', q.queue[0])

n = -1
while n != 0:
    n = int(input())
    if n != 0:
        solve(n)