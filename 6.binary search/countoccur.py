nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
target=3
def firstocc(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ans1=-1
    
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            ans1=mid
            high=mid-1
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return ans1
def lastocc(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ans2=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            ans2=mid
            low=mid+1
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return ans2


def fun(nums,target):
    ans1=firstocc(nums,target)
    if ans1==-1:
        return 0

    ans2=lastocc(nums,target)

    return ans2-ans1+1

print(fun(nums,target))


