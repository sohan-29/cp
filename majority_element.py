n=int(input())
nums=list(map(int,input().split()))
nums.sort()
if nums[n//2]==nums[n//2+1]:
    print(nums[n//2])
else:
    print(-1)
