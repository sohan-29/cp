n = int(input())
nums = list(map(int, input().split()))
c_s = 0
m_s = 0
for num in nums:
    c_s += num
    if c_s > m_s:
        m_s = c_s
    if c_s <= 0:
        c_s = 0
print(m_s)
