def transform(expression):
    s = []
    for symbol in expression:
        if symbol == '(':
            continue
        elif 97 <= ord(symbol) and ord(symbol) <= 122:
            print(symbol, end=' ')
        elif symbol == '+' or symbol == '-' or symbol == '*' or symbol == '/' or symbol == '^':
            s.append(symbol)
        elif symbol == ')':
            value = s.pop()
            print(value, end=' ')
    print()

t = int(input())
for i in range(t):
    expression = input()
    transform(expression)