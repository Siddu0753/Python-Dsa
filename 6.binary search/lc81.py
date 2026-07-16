# nums = [2,5,6,0,0,1,2]
# target = 0

nums =[1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target =2

def binary(nums,target):
    n=len(nums)
    low=0
    high=n-1
    
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        elif nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            if nums[low]==target:
                return True
            elif nums[high]==target:
                return True

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
    return False
print(binary(nums,target))



