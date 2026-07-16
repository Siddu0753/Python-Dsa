nums = [4,5,6,7,0,1,2]
target = 0

def binary(nums,target):
    n=len(nums)
    low=0
    high=n-1
    
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[low]<=nums[mid]: 
            if nums[low]<=target and nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        else:
            if nums[mid]<target and nums[high]>=target:
                low=mid+1
            else:
                high=mid-1
    return -1
print(binary(nums,target))



