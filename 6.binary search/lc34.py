
nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]
target=3
def fun(nums,target):

    n=len(nums)
    low=0
    high=n-1
    fc=0
    lc=0
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            ans=mid
            
            

           

print(fun(nums,target))

