n = int(input())
n1 = list(map(int, input().split()))
m = int(input())
m1 = list(map(int, input().split()))
i = 0
j = 0
res = []
while i < n and j < m:
    if n1[i] <= m1[j]:
        res.append(n1[i])
        i += 1
    else:
        res.append(m1[j])
        j += 1
while i < n:
    res.append(n1[i])
    i += 1
while j < m:
    res.append(m1[j])
    j += 1
print(*res)
