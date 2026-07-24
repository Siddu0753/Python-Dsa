# . Find Minimum in Rotated Sorted Array
# Medium

nums = [3,4,5,1,2]

def fun(nums):
    n=len(nums)
    low=0
    high=n-1

    while low<high:
        mid=(low+high)//2
        if nums[mid]>nums[high]:
            low=mid+1
        else:
            high=mid
    return nums[low]
print(fun(nums))



        




