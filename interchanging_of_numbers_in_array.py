n=int(input())
nums=list(input().split())
mi=min(nums)
ma=max(nums)
mi_c=True
ma_c=True
for i in range(n):
    if nums[i]==mi and mi_c:
        nums[i]=ma
    elif nums[i]==ma and ma_c:
        nums[i]=mi
print(*nums)
