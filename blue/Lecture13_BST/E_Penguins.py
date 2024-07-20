name_freq = {'Emperor Penguin':0, 'Little Penguin':0, 'Macaroni Penguin':0}
n = int(input())
for _ in range(n):
    name = input()
    name_freq[name] += 1
sorted_list = sorted(name_freq.items(), key=lambda item: -item[1])
print(sorted_list[0][0])