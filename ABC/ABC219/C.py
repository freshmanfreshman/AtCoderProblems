a = list(input())
pos = dict()
for i in range(26):
    pos[a[i]] = i

n = int(input())

S = []
for _ in range(n):
    s = list(input())
    for i in range(len(s)):
        s[i] = pos[s[i]]
    S.append(s)
S.sort()

ans = []
for s0 in S:
    s1 = ''
    for j in s0:
        s1 += a[j]
    ans.append(s1)
print(*ans, sep='\n')
