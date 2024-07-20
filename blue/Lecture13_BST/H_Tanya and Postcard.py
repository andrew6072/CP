s = input()
t = input()
s_freq = {}
t_freq = {}


def updateDict(char, dict):
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1


for i in range(len(s)):
    updateDict(s[i], s_freq)

for i in range(len(t)):
    updateDict(t[i], t_freq)

# find yay
num_yay = 0
for i in range(len(s)):
    char = s[i]
    if char in t_freq and char in s_freq:
        freq_char_in_s = s_freq[char]
        freq_char_in_t = t_freq[char]

        if s_freq[char] > t_freq[char]:
            num_yay += t_freq[char]
            s_freq[char] -= t_freq[char]
            del t_freq[char]
        elif s_freq[char] < t_freq[char]:
            num_yay += s_freq[char]
            t_freq[char] -= s_freq[char]
            del s_freq[char]
        else:
            num_yay += t_freq[char]
            del t_freq[char]
            del s_freq[char]

# find whoops
def swap_case(char):
    if char.islower():
        return chr(ord(char) - 32)
    elif char.isupper():
        return chr(ord(char) + 32)
    else:
        return char


num_whoops = 0
for key in s_freq.keys():
    if swap_case(key) in t_freq:
        if s_freq[key] >= t_freq[swap_case(key)]:
            num_whoops += t_freq[swap_case(key)]
        else:
            num_whoops += s_freq[key]

print(num_yay, num_whoops)
