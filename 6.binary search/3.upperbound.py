def lowerbond(nums,target):
  
    n=len(nums)
    ub=n
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub

print(lowerbond([1,1,1,1,2,3,4,5,5,5],1))