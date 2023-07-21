n = int(input())
str = input().strip()
fre = [0]*150
for i in range(len(str)):
    lower_c = str[i].lower()
    ord_c = ord(lower_c)
    fre[ord_c] += 1
ans = "YES"
for i in range(97, 123):
    if fre[i] == 0:
        ans = "NO"

print(ans)