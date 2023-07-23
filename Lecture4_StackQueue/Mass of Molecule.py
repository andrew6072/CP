molecule = input().strip()
mass = lambda c : 1 if c == 'H' else 12 if c == 'C' else 16

stack = []
for c in molecule:
    if c.isdigit():
        a = int(stack.pop())
        stack.append(a * int(c))
    elif c == '(':
        stack.append(-1)
    elif c == ')':
        sum = 0
        while stack[-1] != -1:
            a = int(stack.pop())
            sum += a
        stack.pop()
        stack.append(sum)
    else:
        stack.append(mass(c))

res = 0
while len(stack) != 0:
    res += stack.pop()

print(res)