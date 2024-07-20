import queue

A = "xxikrwmjvsvckfrqxnibkcasompsuyuogauacjrr"

char_dict = [0]*26

a = ""
q = queue.Queue()
for i, c in enumerate(A):
    q.put(c)
    char_dict[ord(c)-ord('a')] += 1
    while not q.empty() and char_dict[ord(q.queue[0])-ord('a')] > 1:
        q.get()
    if q.empty():
        a += '#'
    else:
        a += q.queue[0]

print(a)
