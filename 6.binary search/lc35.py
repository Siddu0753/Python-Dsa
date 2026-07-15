
def searchInsert( nums, target):

        n=len(nums)
        lb=-1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            
            if nums[mid]>=target:
                 lb=mid
                 high=mid-1
            else:
                 low=mid+1

        return lb

print(searchInsert([1,3,5,6],5))

# tc:log base2 n,sc:O(1)

            
