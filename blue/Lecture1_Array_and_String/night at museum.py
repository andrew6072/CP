word = input()
alphabet = [chr(i) for i in range(97, 123)]

move = 0
right = 0
left = 0
for i in range(len(word)):
    count = 0
    while (alphabet[left] != word[i] and alphabet[right] != word[i]):
        right = (right + 1) % len(alphabet)
        left -= 1
        count += 1
    if (alphabet[left] == word[i]):
        if left < 0:
            left = left + len(alphabet)
        right = left
    else:
        left = right
    move += count

print(move)