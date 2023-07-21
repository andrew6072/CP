str = input().strip()

count = 1
for i in range(len(str)):
    if not str[i].islower():
        count += 1
print(count)