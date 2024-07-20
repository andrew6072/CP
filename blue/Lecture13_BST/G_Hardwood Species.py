tc = int(input())
input()

def solve(name_freq, count):
    sorted_dict = dict(sorted(name_freq.items(), key=lambda item: item[0]))
    for item in sorted_dict.items():
        print(item[0], "%.4f" % (item[1] * 100 / count))
    print()

for i in range(tc):
    name_freq = {}
    count = 0
    if i != tc - 1:
        while True:
            name = input()
            if len(name) < 1:
                break
            else:
                if not (name in name_freq):
                    name_freq[name] = 1
                else:
                    name_freq[name] += 1
                count += 1
    else:
        while True:
            try:
                name = input()
                if not (name in name_freq):
                    name_freq[name] = 1
                else:
                    name_freq[name] += 1
                count += 1
            except EOFError:
                break
    solve(name_freq, count)
