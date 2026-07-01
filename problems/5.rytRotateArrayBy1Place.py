nums=[5,-2,3,9,0,6,10,7]
def rytrotate(nums):
    n=len(nums)
    temp=nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0]=temp

    # nums[:]=[nums[-1]]+nums[0:n-1]
    return nums

print(rytrotate(nums))
