n=int(input())
nums=list(map(int,input().split()))
c_s=nums[0]
m_s=c_s
for i in range(1,n):
    if nums[i]>nums[i-1]:
        c_s+=nums[i]
    else:
        c_s=nums[i]
    m_s=max(m_s,c_s)
print(m_s)
