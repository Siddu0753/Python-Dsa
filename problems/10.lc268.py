print("missing number in the array")


nums=[8,6,4,2,3,5,7,0,1]

nums.sort()
def mis(nums):
    n=len(nums)
    for i in range(0,n+1):
        if nums[i]!=i:
            return nums[i]-1
        elif nums[i]==n-1:
            return nums[i]+1
        
print(mis(nums))

        