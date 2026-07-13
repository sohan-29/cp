n=int(input())
nums=list(map(int,input().split()))
freq=[0]*100000
for num in nums:
    freq[num]+=1
res=[]
for i,f in enumerate(freq):
    if num:
        res.extend([i]*f)
print(*res)
